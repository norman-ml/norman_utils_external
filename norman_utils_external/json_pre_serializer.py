from datetime import datetime
from enum import Enum

from norman_utils_external.date_utils import DateUtils


class JsonPreSerializer:
    """
    Utility for converting arbitrary Python objects into JSON-safe,
    serialization-friendly structures. Handles cycles, dataclasses,
    Pydantic models, enums, slots, sensitive fields, and datetime values.
    """

    @staticmethod
    def prepare_for_serialization(context_var):
        """
        Fully normalize an object graph into a JSON-serializable structure.
        Performs a two-pass BFS to:
        - shallow-normalize each node
        - rebuild references to avoid cycles
        - remove private fields
        - convert models/enums/datetimes into JSON-safe values
        """
        # Create an id for the context var (using python id function, not the object id)
        context_var_id = id(context_var)

        # Prevents altering context_var.
        # Structured as a shallow key:value lookup to determine whether a given node is contained within context_car
        node_lookup = {}

        # Facilitates the BFS
        traversal_stack = [(context_var, id(context_var))]

        # Prevents infinite recursion and reference loops
        visited_element_ids = set()

        # First breadth-first-search over the traversal stack to normalize and pre-serialize nodes.
        while len(traversal_stack) > 0:
            current_node, node_id = traversal_stack.pop()
            if node_id in visited_element_ids:
                continue

            visited_element_ids.add(node_id)

            # Normalize and shallow-copy current node. Child nodes will be normalized in following iterations (BFS)
            child_nodes = JsonPreSerializer.shallow_normalize(current_node)

            # Calculate an id for each node, and store as a list of tuples
            stack_elements = JsonPreSerializer.create_stack_elements(child_nodes)

            # Add filtered tuples to traversal stack for iteration
            traversal_stack.extend(stack_elements)

            # Add normalized child nodes to node lookup. Notice that the node_id is of the original node.
            node_lookup[node_id] = child_nodes

        # Restart the BFS
        traversal_stack.append((context_var, id(context_var)))
        visited_element_ids.clear()

        # Second breadth-first-search over the traversal stack to update pointers to the normalized nodes from the first iteration.
        while len(traversal_stack) > 0:
            current_node, node_id = traversal_stack.pop()
            if node_id in visited_element_ids:
                continue

            visited_element_ids.add(node_id)

            # Get pre-serialized node from node lookup, using the node_id of the original node
            pre_serialized_node = node_lookup[node_id]

            # Update refs for dicts to point to the pre-serialized children instead of the original children.
            if isinstance(pre_serialized_node, dict):
                node_children = {key: node_lookup[id(value)] for key, value in pre_serialized_node.items()}

                stack_elements = [(value, id(value)) for value in pre_serialized_node.values()]
                traversal_stack.extend(stack_elements)

                pre_serialized_node.clear()
                pre_serialized_node.update(node_children)

            # Update refs for other collections to point to the pre-serialized children instead of the original children.
            elif isinstance(pre_serialized_node, list):
                node_children = [node_lookup[id(value)] for value in pre_serialized_node]

                stack_elements = [(value, id(value)) for value in pre_serialized_node]
                traversal_stack.extend(stack_elements)

                pre_serialized_node.clear()
                pre_serialized_node.extend(node_children)

        # Return normalized node for use in any serialization library
        return node_lookup[context_var_id]

    @staticmethod
    def shallow_normalize(node):
        """
        Convert a single object into a JSON-safe shallow representation.
        Handles:
        - Sensitive fields → "<redacted>"
        - Enum → enum.value
        - dict/list/tuple/set → shallow copies
        - Pydantic/dataclass (__dict__, __slots__) → dict form
        - datetime → ISO-8601 string
        """

        if hasattr(node, "__sensitive__"):
            return "<redacted>"
        elif isinstance(node, Enum):
            return node.value
        elif isinstance(node, dict):
            return {key: value for key, value in node.items() if not key.startswith("_")}
        elif isinstance(node, (list, tuple, set)):
            return [value for value in node]
        elif hasattr(node, "model_dump") and callable(getattr(node, "model_dump")):
            dict_representation = node.model_dump()
            return dict_representation
        elif hasattr(node, "dict") and callable(getattr(node, "dict")):
            dict_representation = node.dict()
            return dict_representation
        elif hasattr(node, "__slots__"):
            dict_representation = {key: getattr(node, key) for key in node.__slots__ if not key.startswith("_")}
            return dict_representation
        elif hasattr(node, "__dict__"):
            dict_representation = {key: value for key, value in node.__dict__.items() if not key.startswith("_")}
            return dict_representation
        elif hasattr(node, "__items__"):
            node_items = getattr(node, "__items__")
            iterable = JsonPreSerializer.get_iterable(node_items)
            dict_representation = {key: value for key, value in iterable if not key.startswith("_")}
            return dict_representation
        elif isinstance(node, datetime):
            return DateUtils.datetime_to_string(node, DateUtils.iso_8061_format)
        else:
            return node

    @staticmethod
    def get_iterable(variable):
        if callable(variable):
            return variable()
        elif isinstance(variable, dict):
            return variable.items()
        else:
            return variable

    @staticmethod
    def create_stack_elements(node_collection):
        """
        Convert a normalized container (dict/list/tuple/set) into BFS queue
        elements `(child, id(child))` for traversal.
        """
        if isinstance(node_collection, dict):
            stack_elements = [(node, id(node)) for node in node_collection.values()]
            return stack_elements
        elif isinstance(node_collection, (list, tuple, set)):
            stack_elements = [(node, id(node)) for node in node_collection]
            return stack_elements
        else:
            stack_elements = [(node_collection, id(node_collection))]
            return stack_elements

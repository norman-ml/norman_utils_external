import re


class DotSyntaxResolver:
    """
    Utility for resolving and mutating nested structures (dicts, lists, and
    objects) using dot-syntax and bracket notation.

    **Methods**
    """

    @staticmethod
    def get(parent: object, key: str) -> object:
        """
        Retrieve a nested value using dot + bracket syntax such as
        `"a.b[2].c"`. Supports dicts, lists, tuples, and object attributes.
        Raises `KeyError` or `IndexError` if a segment is invalid.

        **Parameters**

        - **parent** (`object`)
            The root object from which resolution begins. May be a dictionary,
            list, tuple, or any object supporting attribute access.

        - **key** (`str`)
            Dot + bracket–notation path used to navigate into the nested structure.

        **Returns**

        - **object** — The resolved nested value. Type depends on the structure.
        """

        if key is not None:
            accessors = re.findall(r"[^\.\[\]]+|\[\d+\]", key)
            deepest_value = parent

            for accessor in accessors:
                if isinstance(deepest_value, (list, tuple)):
                    deepest_value = DotSyntaxResolver.__get_list_child(deepest_value, accessor)
                else:
                    deepest_value = DotSyntaxResolver.__get_dict_child(deepest_value, accessor)

            return deepest_value
        return None

    @staticmethod
    def set(parent: object, key: str, value: object) -> object:
        """
        Set a nested value using dot + bracket syntax, creating intermediate
        dict/list nodes as needed. Supports patterns like `"a.b[0].c = X"`.

        **Parameters**

        - **parent** (`object`)
            A dictionary or list into which the nested value will be written.
            Intermediate containers are created automatically.

        - **key** (`str`)
            Dot + bracket–notation path specifying where the value should be
            assigned.

        - **value** (`object`)
        The value to assign at the target location. Can be any Python object,
        including primitives, dictionaries, lists, or custom types.

        **Returns**

        - **object** — The modified `parent` containing the updated structure.

        **Raises**

        - **ValueError** — If the provided key uses malformed list index syntax
        """

        if not isinstance(parent, (dict, list)):
            raise TypeError("Can only set a value in a dict or list object")

        accessors = re.findall(r"[^\.\[\]]+|\[\d+\]", key)
        deepest_value = parent
        
        for accessor_index in range(len(accessors) - 1):
            accessor = accessors[accessor_index]
            next_accessor = accessors[accessor_index + 1]
            
            if isinstance(deepest_value, list):
                deepest_value = DotSyntaxResolver.__expand_list_child(deepest_value, accessor, next_accessor)
            else:
                deepest_value = DotSyntaxResolver.__expand_dict_child(deepest_value, accessor, next_accessor)

        last_accessor = accessors[-1]
        if isinstance(deepest_value, list):
            DotSyntaxResolver.__set_list_child(deepest_value, last_accessor, value)
        else:
            deepest_value[last_accessor] = value

        return parent

    @staticmethod
    def __get_list_child(parent, accessor: str):
        parent_index = DotSyntaxResolver.__extract_list_index(accessor)
        if len(parent) <= parent_index:
            raise IndexError("Accessor is out of bounds for the given parent")

        child = parent[parent_index]
        return child

    @staticmethod
    def __get_dict_child(parent, accessor: str):
        if hasattr(parent, accessor):
            child = getattr(parent, accessor)
        elif isinstance(parent, dict) and accessor in parent:
            child = parent[accessor]
        else:
            raise KeyError("Accessor is not a property or key of the given parent")

        return child

    @staticmethod
    def __expand_list_child(parent: list, accessor: str, next_accessor: str):
        parent_index = DotSyntaxResolver.__extract_list_index(accessor)
        if len(parent) <= parent_index:
            filler_type = DotSyntaxResolver.__infer_filler_from_accessor(next_accessor)
            parent = DotSyntaxResolver.__fill_list(parent, parent_index + 1, filler_type)
            parent[parent_index] = filler_type()

        return parent[parent_index]

    @staticmethod
    def __expand_dict_child(parent: dict, accessor: str, next_accessor: str):
        if accessor not in parent:
            filler_type = DotSyntaxResolver.__infer_filler_from_accessor(next_accessor)
            parent[accessor] = filler_type()

        return parent[accessor]

    @staticmethod
    def __set_list_child(parent: list, accessor: str, value: object):
        parent_index = DotSyntaxResolver.__extract_list_index(accessor)
        filler_type = type(value)

        DotSyntaxResolver.__fill_list(parent, parent_index + 1, filler_type)
        parent[parent_index] = value

    @staticmethod
    def __extract_list_index(accessor: str):
        if len(accessor) < 3 or accessor[0] != "[" or accessor[-1] != "]":
            raise ValueError("Accessor is a malformed array index")

        stripped_key = accessor[1:-1]
        try:
            list_index = int(stripped_key)
            return list_index
        except ValueError:
            raise ValueError("Accessor does not contain a valid integer index")

    @staticmethod
    def __fill_list(parent: list, new_length: int, fallback_filler_type: type):
        delta = new_length - len(parent)

        if new_length <= 0 or delta <= 0:
            return parent

        if len(parent) <= 0:
            # Note: this only supports primitives and objects with default constructors.
            extension_list = [fallback_filler_type() for _ in range(delta)]
        else:
            first_child = parent[0]
            filler_type = type(first_child)

            # Note: this only supports primitives and objects with default constructors.
            extension_list = [filler_type() for _ in range(delta)]

        parent.extend(extension_list)
        return parent

    @staticmethod
    def __infer_filler_from_accessor(accessor: str):
        if len(accessor) > 2 and accessor[0] == "[" and accessor[-1] == "]":
            return list
        
        return dict
    
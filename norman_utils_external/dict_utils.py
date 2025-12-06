from collections import deque
from typing import Dict, Any

class DictUtils:
    """
    Utility class providing dictionary-related helper functions.

    Currently includes support for performing *deep merges* between nested
    dictionaries, preserving shared structure and recursively merging child
    dictionaries.

    **Methods**
    """

    @staticmethod
    def deep_merge(source_dict: Dict[str, Any], target_dict: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recursively merge the contents of `target_dict` into `source_dict`.

        Unlike a shallow merge, this function walks nested dictionaries and
        merges them level-by-level. Non-dictionary values in `target_dict`
        overwrite values in `source_dict`. Dictionary values are merged
        recursively.

        - This is useful for combining
            - configuration dictionaries
            - JSON-like nested structures
            - partial updates
            - schema or settings overlays

        - If a key exists in both dictionaries
            - If both values are dictionaries - merge recursively.
            - Otherwise - value from `target_dict` replaces value in `source_dict`.

        - If a key exists only in `target_dict`
            - It is added to `source_dict`.

        **Parameters**

        - **source_dict** (`Dict[str, Any]`)
          The base dictionary that will be updated in-place.
          Returned after merging.

        - **target_dict** (`Dict[str, Any]`)
          The dictionary whose keys and values are merged into
          `source_dict`.

        **Returns**

        - **Dict[str, Any]** - The updated `source_dict` after merging.
        """
        node_queue = deque()
        node_queue.append((source_dict, target_dict))

        while len(node_queue) > 0:
            source_node, target_node = node_queue.popleft()

            if target_node is None:
                continue

            for target_key, target_value in target_node.items():
                if target_key in source_node:
                    source_value = source_node[target_key]
                    if isinstance(source_value, dict) and isinstance(target_value, dict):
                        node_queue.append((source_value, target_value))
                else:
                    source_node[target_key] = target_value

        return source_dict



from collections import deque
from typing import Dict, Any

class DictUtils:

    @staticmethod
    def deep_merge(source_dict: Dict[str, Any], target_dict: Dict[str, Any]):
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


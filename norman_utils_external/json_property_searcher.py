from collections import deque
from typing import Union


class JsonPropertySearcher:

    @staticmethod
    def search(source: dict, keys: Union[set, list, tuple]):
        results = {}
        remaining_keys = set(keys)
        queue = deque([source])

        while len(queue) > 0 and len(remaining_keys) > 0:
            current_node = queue.popleft()

            if isinstance(current_node, dict):
                for key, value in current_node.items():
                    if key in remaining_keys:
                        results[key] = value
                        remaining_keys.discard(key)

                    queue.append(value)

            elif isinstance(current_node, (set, list, tuple)):
                queue.extend(current_node)

        return results
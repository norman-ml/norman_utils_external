from collections import deque


class JsonPropertySearcher:

    @staticmethod
    def search(source: dict, keys: set):
        results = {}
        remaining_keys = set(keys)
        queue = deque([source])

        while len(queue) > 0 and len(remaining_keys) > 0:
            current = queue.popleft()

            if isinstance(current, dict):
                for key, value in current.items():
                    if key in remaining_keys:
                        results[key] = value
                        remaining_keys.discard(key)
                    queue.append(value)

            elif isinstance(current, (list, tuple)):
                queue.extend(current)

        return results
from collections import deque


class JsonPropertySearcher:

    @staticmethod
    def search(source: dict, keys: set):
        results = {}
        remaining = set(keys)
        queue = deque([source])

        while queue and remaining:
            current = queue.popleft()

            if isinstance(current, dict):
                for key, value in current.items():
                    if key in remaining:
                        results[key] = value
                        remaining.discard(key)
                        if not remaining:
                            return results
                    queue.append(value)

            elif isinstance(current, (list, tuple)):
                queue.extend(current)

        return results

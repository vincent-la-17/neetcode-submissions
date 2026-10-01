class TimeMap:

    def __init__(self):
        # Dictionary where each key maps to a list of [value, timestamp] pairs
        self.tracker = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key doesn't exist yet, create an empty list for it
        if key not in self.tracker:
            self.tracker[key] = []

        # Store the value and timestamp for this key
        # Timestamps are added in increasing order
        self.tracker[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Default result is an empty string if no valid timestamp is found
        # Get the list of [value, timestamp] pairs for the given key
        res, values = "", self.tracker.get(key, [])

        # Binary search for the largest timestamp <= the given timestamp
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2

            # If the current timestamp is valid, save its value as the result
            # and search to the right for a later valid timestamp
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1

            # If the current timestamp is too large, search the left half
            else:
                r = m - 1

        # Return the value associated with the latest timestamp <= timestamp
        return res
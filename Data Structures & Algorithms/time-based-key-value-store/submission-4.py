class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        timestamps = self.keyStore.get(key, [])
        l, r = 0, len(timestamps) - 1
        while l <= r:
            mid = (l + r) // 2
            if timestamps[mid][1] <= timestamp:
                res = timestamps[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res

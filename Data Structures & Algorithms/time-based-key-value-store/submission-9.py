class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""
        res = ""
        values = self.keyStore[key]

        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            time = values[mid][0]
            if time <= timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res 

        
        

class TimeMap:

    def __init__(self):
        self.store = {} # {k:[[v0, t0], [v1, t1] ... ]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
            
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        values = self.store[key]
        l, r = 0, len(values) - 1
        result = ""

        while l <= r:
            mid = l + (r - l) // 2
            t = values[mid][1]

            if t == timestamp:
                return values[mid][0]
            elif t > timestamp:
                r = mid - 1
            else:
                result = values[mid][0] # save the candidate
                l = mid + 1             # search for a later timestamp

        return result
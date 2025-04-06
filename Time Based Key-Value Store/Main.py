from typing import List

class TimeMap:
    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = [(timestamp, value)]
        else:
            self.timeMap[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.timeMap:
            return res
        else:
            temp = self.timeMap[key]
            l, r = 0, len(temp) - 1
            
            while l <= r:
                mid = (l + r) // 2

                if timestamp == temp[mid][0]:
                    return self.timeMap[key][mid][1]
                elif timestamp < temp[mid][0]:
                    r = mid - 1
                else:
                    l = mid + 1
            if l >= len(temp):
                return self.timeMap[key][r][1]
            elif l< len(temp) and timestamp >= temp[l][0]:
                return self.timeMap[key][l][1]
            else:
                return res

if __name__ == "__main__":
    timemap = TimeMap()
    timemap.set("key", "value1", 10)
    print(timemap.get("key", 1))
    print(timemap.get("key", 10))
    print(timemap.get("key", 11))


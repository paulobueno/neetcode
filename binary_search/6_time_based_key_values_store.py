# URL https://neetcode.io/problems/time-based-key-value-store
# Time Complexity: O(log(n))
# Space Complexity: O(n)

from typing import List

class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key] = self.data.get(key, [])
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        data = self.data.get(key,[])
        if not data:
            return ""
        l, r = 0, len(data) - 1
        while l <= r:
            m = l+((r-l)//2)
            if data[m][0] == timestamp:
                return data[m][1]
            if timestamp < data[m][0]:
                r = m - 1
            else:
                l = m + 1
        if l > len(data):
            return data[-1][1]
        elif r < 0:
            return ""
        else:
            return data[min(l,r)][1]


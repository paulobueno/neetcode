# URL https://neetcode.io/problems/car-fleet
# Time Complexity: O(Nlog(N))
# Space Complexity: O(N)

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [x for x in zip(position, speed)]
        stack = sorted(stack, key=lambda x: x[0])
        previews_time_to_target = None
        fleets = 0

        while stack:
            car = stack.pop()
            time_to_target = (target - car[0]) / car[1]

            if previews_time_to_target is None:
                previews_time_to_target = time_to_target
                fleets += 1
                continue

            if time_to_target > previews_time_to_target:
                fleets += 1
                previews_time_to_target = time_to_target

        return fleets

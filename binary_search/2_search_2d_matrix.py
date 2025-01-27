# URL https://neetcode.io/problems/search-2d-matrix
# Time Complexity: O(log(N))
# Space Complexity: O(1)

from typing import List


class Solution:
    def binary_search(self, elements, target) -> int:
        l, r = 0, len(elements)
        while l < r:
            m = l + ((r - l) // 2)
            if elements[m] >= target:
                r = m
            else:
                l = m + 1
        return l if l < len(elements) and elements[l] == target else -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)
        while l < r:
            m = l + ((r - l) // 2)
            if matrix[m][0] <= target <= matrix[m][-1]:
                return self.binary_search(matrix[m], target) != -1
            elif target < matrix[m][0]:
                r = m
            else:
                l = m + 1
        return False

if __name__ == '__main__':
    print(Solution().searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10) == True)
    print(Solution().searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15) == False)

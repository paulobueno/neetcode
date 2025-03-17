# URL https://neetcode.io/problems/count-connected-components
# Time Complexity: O(m*n) m -> rows n -> columns
# Space Complexity: O(m*n)

from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        roots = [i for i in range(n)]
        rank = [1] * n
        components = n
        
        def find_root(i):
            # Path compression
            cur = i
            while cur != roots[cur]:
                cur = roots[cur]
            return cur
        
        def union(i, j):
            root_i = find_root(i)
            root_j = find_root(j)
            
            if root_i == root_j:
                return False
                
            if rank[root_i] >= rank[root_j]:
                roots[root_j] = root_i
                rank[root_i] += rank[root_j]
            else:
                roots[root_i] = root_j
                rank[root_j] += rank[root_i]
            return True
        
        for i, j in edges:
            if union(i, j):
                components -= 1
                
        return components

if __name__ == "__main__":
    n = 5
    edges = [[0, 1], [1, 2], [3, 4], [2, 3], [1, 4]]
    print(Solution().countComponents(n, edges)) # 1

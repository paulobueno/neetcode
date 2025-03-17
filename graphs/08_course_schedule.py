# URL https://neetcode.io/problems/course-schedule
# Time Complexity: O(m*n) m -> rows n -> columns
# Space Complexity: O(m*n)

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses_map = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            courses_map[course].append(prereq)

        visited = set()
        def dfs(course):
            if not courses_map[course]:
                return True
            if course in visited:
                return False

            visited.add(course)
            for prereq in courses_map[course]:
                if dfs(prereq) is False:
                    return False
            visited.remove(course)
            courses_map[course] = []
            return True

        for course in range(numCourses):
            if dfs(course) is False:
                return False

        return True



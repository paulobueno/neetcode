# URL https://neetcode.io/problems/course-schedule-ii
# Time Complexity: O(m*n) m -> rows n -> columns
# Space Complexity: O(m*n)

from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses_map = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            courses_map[course].append(prereq)

        output = []
        visited, visiting = set(), set()

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)
            for i in courses_map[course]:
                if dfs(i) is False:
                    return False
            visiting.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for i in range(numCourses):
            if dfs(i) is False:
                return []

        return output

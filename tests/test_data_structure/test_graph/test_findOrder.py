import unittest
from collections import defaultdict, deque

def findOrder(numCourses, prerequisites):
    # assert 0--> 1
    #        0 --> 2  2-->3
    #  [0,1,2,3] 

    # construct a graph
    # indegree

    # bfs graph to turn result
    # get init by indegrere

    result = []
    graph = defaultdict(list)
    queue = deque()
    indegree = [0] * numCourses

    for dep, pre in prerequisites:
        graph[pre].append(dep)
        indegree[dep] += 1

    # put nodes with 0 indegree to queue
    for n in range(numCourses):
        if indegree[n] == 0:
            queue.append(n)

    while queue:
        course = queue.popleft()
        result.append(course)

        for dep in graph[course]:
            indegree[dep] -= 1
            if indegree[dep] == 0:
                queue.append(dep)

    if len(result) == numCourses:
        return result
    else:
        return []


def findOrderDFS(numCourses, prerequisites):
    # assert 0--> 1
    #        0 --> 2  2-->3
    #  [0,1,2,3] 

    # construct a graph
    # indegree

    # bfs graph to turn result
    # get init by indegrere

    result = []
    visited = {0 for _ in range(numCourses)} #-1 visiting 0 not visited 1 visited
    graph = defaultdict(list)

    def dfs(n):
        """
        This function returns True if no circle is detected there is circle and add node along the way
        """
        if visited[n] == -1:
            return False
        if visited[n] == 1:
            return True
        visited[nei] == -1
        
        for nei in graph[n]:
            if not dfs(nei):
                return False
                
        result.append(n)
        visited[n] = 1
        return True

    for dep, pre in prerequisites:
        graph[pre].append(dep)
    # put nodes with 0 indegree to queue
    for n in range(numCourses):
        if visited[n] == 0:
            if not dfs(n):
                return []

    return result[::-1]

class TestFindOrder(unittest.TestCase):
    
    def test_simple_linear_order(self):
        """Test with simple linear dependency: 1 -> 0"""
        numCourses = 2
        prerequisites = [[1, 0]]
        result = findOrder(numCourses, prerequisites)
        self.assertEqual(result, [0, 1])
    
    def test_no_prerequisites(self):
        """Test with no prerequisites - any order is valid"""
        numCourses = 4
        prerequisites = []
        result = findOrder(numCourses, prerequisites)
        self.assertEqual(len(result), 4)
        self.assertEqual(set(result), {0, 1, 2, 3})
    
    def test_cycle_impossible(self):
        """Test with circular dependency - should return empty array"""
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        result = findOrder(numCourses, prerequisites)
        self.assertEqual(result, [])
    
    def test_complex_valid_order(self):
        """Test with complex but valid dependencies"""
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        result = findOrder(numCourses, prerequisites)
        # Valid orders: [0,1,2,3] or [0,2,1,3]
        self.assertTrue(result in [[0, 1, 2, 3], [0, 2, 1, 3]])
    
    def test_single_course(self):
        """Test with single course and no prerequisites"""
        numCourses = 1
        prerequisites = []
        result = findOrder(numCourses, prerequisites)
        self.assertEqual(result, [0])


if __name__ == '__main__':
    unittest.main()
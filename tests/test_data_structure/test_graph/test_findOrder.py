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
    def enque_children(queue, indegree, dep):
        if indegree[dep] == 0:
            queue.append(dep)

    def remove_edge_from_graph(indegree, dep):
        indegree[dep] -= 1

    def add_zero_indegree_nodes_to_queue(numCourses, queue, indegree):
        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)
    
    result = []
    graph = defaultdict(list)
    queue = deque()
    indegree = [0] * numCourses

    for dep, pre in prerequisites:
        graph[pre].append(dep)
        indegree[dep] += 1

    add_zero_indegree_nodes_to_queue(numCourses, queue, indegree)

    while queue:
        course = queue.popleft()
        result.append(course)

        for dep in graph[course]:
            remove_edge_from_graph(indegree, dep)
            enque_children(queue, indegree, dep)

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
    visited = [0 for _ in range(numCourses)] #-1 visiting 0 not visited 1 visited
    graph = defaultdict(list)
    
    def traverse_all_unmarked_node():
        for n in range(numCourses):
            if visited[n] == 0:
                if not dfs(n):
                    return []
        else:
            return result[::-1]

    def dfs(n):
        """
        This function returns True if no circle is detected there is circle and add node along the way
        """

        def mark_with_temp():
            visited[n] = -1

        def mark_with_permanent():
            visited[n] = 1
        
        if visited[n] == -1:
            return False
        if visited[n] == 1:
            return True
        
        mark_with_temp()
        for nei in graph[n]:
            if not dfs(nei):
                return False
        mark_with_permanent()
        result.append(n)
        return True

    for dep, pre in prerequisites:
        graph[pre].append(dep)
    
    return traverse_all_unmarked_node()

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
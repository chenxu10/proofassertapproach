import pytest

def canFinish(num_course, courses):
    visited = [0] * num_course

    def build_graphs_from(num_course, courses):
        course_graph = [[] for _ in range(num_course)]
        for cor, pre in courses:
            course_graph[pre].append(cor)
        return course_graph
    
    def has_cycle(course):
        """
        Returns boolean to detect there's cycle or not
        """
        if visited[course] == -1:
            return False
        if visited[course] == 1:
            return True
        
        visited[course] = -1
        for nei in course_graph[course]:
            if has_cycle(nei):
                return True
        visited[course] = 1
        return False
    

    def traverse_not_visited(num_course):
        for i in range(num_course):
            if visited[i] == 0:
                if has_cycle(courses[i]):
                    return False
        else:
            return True
    
    course_graph = build_graphs_from(num_course, courses)
    return traverse_not_visited(num_course)

class TestCourseSchedule:
    
    def test_no_prerequisites(self):
        """Test case with no prerequisites - should always be possible"""
        assert canFinish(2, []) == True
    
    def test_simple_valid_case(self):
        """Test simple valid case: course 1 before course 0"""
        assert canFinish(2, [[1, 0]]) == True
    
    def test_simple_cycle(self):
        """Test simple cycle: course 0 needs 1, course 1 needs 0"""
        assert canFinish(2, [[1, 0], [0, 1]]) == False
    
    def test_linear_chain(self):
        """Test linear chain of prerequisites"""
        assert canFinish(4, [[1, 0], [2, 1], [3, 2]]) == True
    
    def test_complex_valid_dag(self):
        """Test complex valid directed acyclic graph"""
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        assert canFinish(4, prerequisites) == True
    
    def test_complex_cycle(self):
        """Test complex case with cycle"""
        prerequisites = [[1, 0], [2, 1], [0, 2]]
        assert canFinish(3, prerequisites) == False
    
    def test_single_course(self):
        """Test single course with no prerequisites"""
        assert canFinish(1, []) == True
    
    def test_self_prerequisite(self):
        """Test course requiring itself as prerequisite"""
        assert canFinish(1, [[0, 0]]) == False
    
    def test_large_valid_case(self):
        """Test larger valid case"""
        prerequisites = [[1, 0], [2, 0], [3, 1], [4, 2], [5, 3], [5, 4]]
        assert canFinish(6, prerequisites) == True
    
    def test_disconnected_components(self):
        """Test multiple disconnected components"""
        prerequisites = [[1, 0], [3, 2]]
        assert canFinish(4, prerequisites) == True
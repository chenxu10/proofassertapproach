import pytest


def canFinish(numCourses, prerequisites):
    """
    Determine if it's possible to finish all courses given prerequisites.
    
    Args:
        numCourses (int): Total number of courses labeled from 0 to numCourses-1
        prerequisites (List[List[int]]): List of prerequisite pairs [a, b] where 
                                       course b must be taken before course a
    
    Returns:
        bool: True if all courses can be finished, False otherwise
    """

    # High level: use dfs to detect for circle, data structure should
    # use visited -1,0,1 three stature


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
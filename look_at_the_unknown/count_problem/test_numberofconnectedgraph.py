import pytest


def countComponents(n, edges):
    """
    Count the number of connected components in an undirected graph.
    
    Args:
        n (int): Number of nodes (0 to n-1)
        edges (List[List[int]]): List of edges where edges[i] = [a, b]
        
    Returns:
        int: Total number of connected components
    """
    pass


class TestNumberOfConnectedGraph:
    
    def test_single_component(self):
        """Test graph with all nodes connected (single component)"""
        n = 5
        edges = [[0, 1], [1, 2], [3, 4]]
        assert countComponents(n, edges) == 2
    
    def test_multiple_components(self):
        """Test graph with multiple disconnected components"""
        n = 5
        edges = [[0, 1], [2, 3]]
        assert countComponents(n, edges) == 3
    
    def test_no_edges(self):
        """Test graph with no edges (all nodes isolated)"""
        n = 4
        edges = []
        assert countComponents(n, edges) == 4
    
    def test_fully_connected(self):
        """Test fully connected graph"""
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        assert countComponents(n, edges) == 1
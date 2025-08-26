import pytest


def validTree(n, edges):
    """
    Check whether edges make up a valid tree with n nodes (0 to n-1).
    
    A valid tree must satisfy:
    1. Connected: all nodes are reachable
    2. Acyclic: no cycles (exactly n-1 edges)
    
    Args:
        n (int): Number of nodes labeled 0 to n-1
        edges (List[List[int]]): List of undirected edges [u, v]
        
    Returns:
        bool: True if edges form a valid tree, False otherwise
    """
    # HINT 1: What's the first property you can check quickly?
    # A tree with n nodes must have exactly _____ edges. Why?
    # Fill in: if len(edges) != _____: return False
    
    # HINT 2: How do you represent the graph for traversal?
    # Consider using an adjacency list. What data structure would you use?
    # Fill in: graph = _____ # Think: defaultdict, regular dict, or list?
    
    # HINT 3: Build your adjacency list
    # Remember: undirected graph means if there's edge (u,v), both u->v and v->u exist
    # Fill in the loop:
    # for u, v in edges:
    #     graph[u]._____
    #     graph[v]._____
    
    # HINT 4: Choose your traversal algorithm
    # You need to check connectivity. What are your options? (DFS, BFS, Union-Find)
    # For learning purposes, try DFS or BFS first. Which feels more natural to you?
    
    # HINT 5: Track visited nodes
    # Fill in: visited = _____  # What data structure tracks unique items efficiently?
    
    # HINT 6: Start traversal from node 0
    # If you chose DFS: use a stack (or recursion)
    # If you chose BFS: use a queue
    # Fill in your traversal logic here
    
    # HINT 7: After traversal, what should you check?
    # A connected graph with n nodes should have visited _____ nodes
    # Fill in: return len(visited) == _____
    
    # BONUS CHALLENGE: Can you implement this using Union-Find?
    # Think about how Union-Find naturally detects cycles during edge addition
    
    pass


class TestValidGraphTree:
    
    def test_valid_tree(self):
        """Test a valid tree structure"""
        n = 5
        edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
        assert validTree(n, edges) == True
    
    def test_cycle_detection(self):
        """Test graph with cycle (not a tree)"""
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
        assert validTree(n, edges) == False
    
    def test_disconnected_graph(self):
        """Test disconnected graph (not a tree)"""
        n = 4
        edges = [[0, 1], [2, 3]]
        assert validTree(n, edges) == False
    
    def test_single_node(self):
        """Test single node with no edges"""
        n = 1
        edges = []
        assert validTree(n, edges) == True
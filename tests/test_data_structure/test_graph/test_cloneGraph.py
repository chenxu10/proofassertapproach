import pytest
from typing import List, Optional

class Node:
    def __init__(self, val: int = 0, neighbors: List['Node'] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: Optional[Node]) -> Optional[Node]:
    r"""
    Given a node in a connected undirected graph, return a deep copy of the graph.
    
    Each node in the graph contains an integer value and a list of its neighbors.
    The graph is represented as an adjacency list where each list describes 
    the set of neighbors of a node in the graph.
    
    Args:
        node: Optional[Node] - reference to a node in the original graph
    
    Returns:
        Optional[Node] - reference to the cloned node in the new graph
    
    Example: adjacency list = [[2,4],[1,3],[2,4],[1,3]]
             Graph: 1---2
                    |   |
                    4---3
    
                    cloneGraph(node1)
                           |
                   DFS/BFS traversal with visited tracking
                      /        |        \        \
               Visit node1  Visit node2  Visit node3  Visit node4
                   |            |            |            |
              Create clone1  Create clone2  Create clone3  Create clone4
                   |            |            |            |
              Store in map   Store in map   Store in map   Store in map
              {1: clone1}    {2: clone2}    {3: clone3}    {4: clone4}
                   |            |            |            |
               Build neighbors: clone1.neighbors = [clone2, clone4]
                              clone2.neighbors = [clone1, clone3]
                              clone3.neighbors = [clone2, clone4]
                              clone4.neighbors = [clone1, clone3]
    
    DFS Traversal Tree:
                    node1
                   /     \
               node2   node4
                 |       |
               node3   node3
                 |       |
               node4   node2
               (visited) (visited)
               
    Clone Mapping:
    Original → Clone
    node1 → clone1 (val=1, neighbors=[clone2, clone4])
    node2 → clone2 (val=2, neighbors=[clone1, clone3])
    node3 → clone3 (val=3, neighbors=[clone2, clone4])
    node4 → clone4 (val=4, neighbors=[clone1, clone3])
    """
    if not node:
        return None
    
    visited = {}
    
    def dfs(original_node):
        # Check visited
        if original_node in visited:
            return visited[original_node]
        # Actual operation
        cloned_node = Node(original_node.val)
        # Add to visited
        visited[original_node] = cloned_node
        # Recursive dfs logic
        for nei in original_node.neighbors:
            cloned_nei = dfs(nei)
            cloned_node.neighbors.append(cloned_nei)

        return cloned_node
    
    return dfs(node)

class TestCloneGraph:
    def test_four_node_cycle(self):
        """Test with 4-node cycle graph"""
        # Create original graph: 1---2
        #                        |   |
        #                        4---3
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        
        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node1, node3]
        
        # Clone the graph
        cloned = cloneGraph(node1)
        
        # Verify structure
        assert cloned is not None
        assert cloned.val == 1
        assert cloned is not node1  # Different object
        assert len(cloned.neighbors) == 2
        
        # Verify all nodes are cloned correctly
        visited = set()
        def verify_clone(original, cloned_node):
            if original.val in visited:
                return
            visited.add(original.val)
            
            assert cloned_node.val == original.val
            assert cloned_node is not original
            assert len(cloned_node.neighbors) == len(original.neighbors)
            
            for orig_neighbor, cloned_neighbor in zip(original.neighbors, cloned_node.neighbors):
                assert cloned_neighbor.val == orig_neighbor.val
                assert cloned_neighbor is not orig_neighbor
        
        verify_clone(node1, cloned)
    
    def test_single_node(self):
        """Test with single node graph"""
        node1 = Node(1)
        cloned = cloneGraph(node1)
        
        assert cloned is not None
        assert cloned.val == 1
        assert cloned is not node1
        assert len(cloned.neighbors) == 0
    
    def test_two_node_graph(self):
        """Test with two connected nodes"""
        node1 = Node(1)
        node2 = Node(2)
        node1.neighbors = [node2]
        node2.neighbors = [node1]
        
        cloned = cloneGraph(node1)
        
        assert cloned is not None
        assert cloned.val == 1
        assert cloned is not node1
        assert len(cloned.neighbors) == 1
        assert cloned.neighbors[0].val == 2
        assert cloned.neighbors[0] is not node2
        assert cloned.neighbors[0].neighbors[0] is cloned
    
    def test_triangle_graph(self):
        """Test with triangular graph"""
        # Create triangle: 1---2
        #                   \ /
        #                    3
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        
        node1.neighbors = [node2, node3]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node1, node2]
        
        cloned = cloneGraph(node1)
        
        assert cloned is not None
        assert cloned.val == 1
        assert len(cloned.neighbors) == 2
        
        # Verify triangle structure is preserved
        cloned_nodes = {cloned.val: cloned}
        for neighbor in cloned.neighbors:
            cloned_nodes[neighbor.val] = neighbor
        
        for neighbor in cloned.neighbors:
            for nested_neighbor in neighbor.neighbors:
                cloned_nodes[nested_neighbor.val] = nested_neighbor
        
        assert len(cloned_nodes) == 3
        for val in [1, 2, 3]:
            assert val in cloned_nodes
            assert len(cloned_nodes[val].neighbors) == 2
    
    def test_empty_graph(self):
        """Test with None input"""
        cloned = cloneGraph(None)
        assert cloned is None
    
    def test_linear_graph(self):
        """Test with linear chain of nodes"""
        # Create chain: 1---2---3---4
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        
        node1.neighbors = [node2]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node3]
        
        cloned = cloneGraph(node1)
        
        assert cloned is not None
        assert cloned.val == 1
        
        # Traverse the cloned chain
        current = cloned
        values = [current.val]
        prev = None
        
        while len(current.neighbors) > 0:
            next_node = None
            for neighbor in current.neighbors:
                if neighbor != prev:
                    next_node = neighbor
                    break
            if next_node is None:
                break
            prev = current
            current = next_node
            values.append(current.val)
        
        assert values == [1, 2, 3, 4]

def build_graph_from_adjacency_list(adj_list: List[List[int]]) -> Optional[Node]:
    """Helper function to build graph from adjacency list for testing"""
    if not adj_list:
        return None
    
    nodes = {}
    for i, neighbors in enumerate(adj_list):
        node_val = i + 1
        if node_val not in nodes:
            nodes[node_val] = Node(node_val)
    
    for i, neighbors in enumerate(adj_list):
        node_val = i + 1
        for neighbor_val in neighbors:
            if neighbor_val not in nodes:
                nodes[neighbor_val] = Node(neighbor_val)
            nodes[node_val].neighbors.append(nodes[neighbor_val])
    
    return nodes[1] if 1 in nodes else None

def graph_to_adjacency_list(node: Optional[Node]) -> List[List[int]]:
    """Helper function to convert graph back to adjacency list for verification"""
    if not node:
        return []
    
    visited = set()
    adj_list = {}
    
    def dfs(current):
        if current.val in visited:
            return
        visited.add(current.val)
        adj_list[current.val] = [neighbor.val for neighbor in current.neighbors]
        for neighbor in current.neighbors:
            dfs(neighbor)
    
    dfs(node)
    
    if not adj_list:
        return []
    
    max_val = max(adj_list.keys())
    result = [[] for _ in range(max_val)]
    for val, neighbors in adj_list.items():
        result[val - 1] = sorted(neighbors)
    
    return result


if __name__ == "__main__":
    test_suite = TestCloneGraph()
    
    print("Running clone graph tests...")
    print("=" * 50)
    
    try:
        test_suite.test_four_node_cycle()
        print("✓ test_four_node_cycle passed")
    except Exception as e:
        print(f"✗ test_four_node_cycle failed: {e}")
    
    try:
        test_suite.test_single_node()
        print("✓ test_single_node passed")
    except Exception as e:
        print(f"✗ test_single_node failed: {e}")
    
    try:
        test_suite.test_two_node_graph()
        print("✓ test_two_node_graph passed")
    except Exception as e:
        print(f"✗ test_two_node_graph failed: {e}")
    
    try:
        test_suite.test_triangle_graph()
        print("✓ test_triangle_graph passed")
    except Exception as e:
        print(f"✗ test_triangle_graph failed: {e}")
    
    try:
        test_suite.test_empty_graph()
        print("✓ test_empty_graph passed")
    except Exception as e:
        print(f"✗ test_empty_graph failed: {e}")
    
    try:
        test_suite.test_linear_graph()
        print("✓ test_linear_graph passed")
    except Exception as e:
        print(f"✗ test_linear_graph failed: {e}")
    
    print("=" * 50)
    print("All tests completed!")
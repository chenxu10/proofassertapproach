import pytest
from typing import List, Optional

class Node:
    def __init__(self, val: int = 0, neighbors: List['Node'] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: Optional[Node]) -> Optional[Node]:
    """
    deep copy
    """

    def dfs(original_node):
        """
        clone vals and neighbors
        """
        def recursive_operation_on_neighbors_of(original_node, clone_node):
            for nei in original_node.neighbors:
                clone_node.neighbors.append(dfs(nei))

        if original_node in visited:
            return visited[original_node]
        else:
            clone_node = Node(original_node.val)
            recursive_operation_on_neighbors_of(original_node, clone_node)
            visited[original_node] = clone_node
            return clone_node

    visited = {}
    if node is None:
        return None
    else:
        return dfs(node)

class TestCloneGraph:
    
    def test_null_input(self):
        """Boundary test: null input handling"""
        # SETUP: Pass None to cloneGraph function
        # EXPECTED: Function should return None without crashing
        # ASSERTIONS TO IMPLEMENT:
        #   result = cloneGraph(None)
        #   assert result is None
        result = cloneGraph(None)
        assert result is None

    
    def test_single_isolated_node(self):
        """Base case: single node with no connections"""
        node = Node(1)
        clone_node = cloneGraph(node)
        assert len(clone_node.neighbors) == 0

    
    def test_triangle_complete(self):
        """Simple cycle: triangular graph"""
        # SETUP: Create triangle where each node connects to the other two
        #   Graph structure: 1---2
        #                     \ /
        #                      3
        # ACTION: Clone starting from node1
        # EXPECTED: Complete triangle clone with preserved relationships
        # ASSERTIONS TO IMPLEMENT:
        #   - Create original triangle with 3 nodes
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        #   - Each node connects to the other 2 nodes
        node1.neighbors = [node2,node3]
        node2.neighbors = [node1,node3]
        node3.neighbors = [node2,node3]
        #   - Clone the graph starting from node1
        #   - Verify cloned node1 exists and has correct value

        #   - Verify cloned node1 is different object from original

        #   - Verify cloned node1 has 2 neighbors


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
    
    print("Clone Graph Test Suite")
    print("Following Laws of Nature in Algorithm Design")
    print("=" * 60)
    
    # Essential test cases for training (following 7±2 cognitive limit)
    essential_tests = [
        "test_null_input",
        "test_single_isolated_node", 
        "test_triangle_complete"
    ]
    
    total_passed = 0
    total_tests = 0
    
    print("\nEssential Test Cases:")
    print("-" * 40)
    
    for test_name in essential_tests:
        try:
            test_method = getattr(test_suite, test_name)
            test_method()
            print(f"  ✓ {test_name}")
            total_passed += 1
        except Exception as e:
            print(f"  ✗ {test_name}: {e}")
        except NotImplementedError:
            print(f"  - {test_name}: TODO (not implemented)")
        total_tests += 1
    
    print("\n" + "=" * 60)
    print(f"Test Results: {total_passed}/{total_tests} passed")
    print("Essential test suite for training:")
    print("• Boundary case: null input")
    print("• Base case: single node") 
    print("• Fundamental pattern: triangle cycle")
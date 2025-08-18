import pytest
from typing import List, Optional

class Node:
    def __init__(self, val: int = 0, neighbors: List['Node'] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: Optional[Node]) -> Optional[Node]:
    r"""
    Clone Graph Algorithm - Deep copy of undirected graph
    
    COMPLEXITY ANALYSIS (Master Theorem Application):
    Time: O(V + E) where V = vertices, E = edges
    Space: O(V) for visited dictionary and recursion stack
    
    ALGORITHM PATTERN: DFS with Memoization
    - Visit each node exactly once: O(V)
    - Process each edge exactly twice (bidirectional): O(E)  
    - Total: O(V + E)
    
    This does NOT fit Master Theorem form T(n) = aT(n/b) + f(n)
    because it's graph traversal, not divide-and-conquer.
    
    COGNITIVE LOAD ANALYSIS:
    - Function parameters: 1 (follows 7±2 rule)
    - Nesting depth: 2 levels (within cognitive limits)
    - Single responsibility: clone graph structure
    
    Args:
        node: Optional[Node] - entry point to graph
    
    Returns:
        Optional[Node] - entry point to cloned graph
        
    ALGORITHM INVARIANTS:
    1. Each original node maps to exactly one clone
    2. Clone preserves all neighbor relationships  
    3. Clone nodes are independent objects
    4. Graph connectivity is preserved
    
    IMPLEMENTATION GUIDANCE (Following Laws of Nature):
    
    1. BASE CASE (Law of Error Proneness):
       # Handle null input to prevent crashes
       # TODO: Check if node is None, return None if so
    
    2. MEMOIZATION SETUP (Law of Limited Working Memory):
       # Use dictionary to track visited nodes (original -> clone mapping)  
       # TODO: Create empty dictionary to store visited nodes
    
    3. DFS HELPER FUNCTION (Law of Chunking):
       # Separate recursive logic into helper function
       # TODO: Define inner function dfs(original_node) that:
       #   a) Checks if node already visited (return cached clone)
       #   b) Creates new clone with same value
       #   c) Stores clone in visited map
       #   d) Recursively processes all neighbors
       #   e) Returns completed clone
    
    4. RECURSIVE PATTERN (Law of Sequential Processing):
       # Follow consistent order: check -> create -> store -> recurse -> return
       # TODO: In dfs helper:
       #   - First: if original_node in visited: return visited[original_node]
       #   - Second: cloned_node = Node(original_node.val)
       #   - Third: visited[original_node] = cloned_node
       #   - Fourth: for each neighbor, recursively clone and append
       #   - Fifth: return cloned_node
    
    5. MAIN FUNCTION CALL (Law of Pattern Recognition):
       # TODO: Call dfs(node) and return result
    
    COMMON ERRORS TO AVOID (Law of Error Proneness):
    - Forgetting to handle None input
    - Creating infinite recursion (store clone BEFORE processing neighbors)
    - Using wrong data structures for visited tracking
    - Forgetting to connect cloned neighbors properly
    """

    if not node:
        return None

    visited = {}

    def dfs(original_node):
        if original_node in visited:
            return visited[original_node]
        else:
            # clone
            clone_node = Node(original_node)
            # add to visit
            visited[original_node] = clone_node

            for nei in original_node.neighbors:
                dfs(nei)
                visited.add(nei)

        return clone_node
    
    return dfs(node)


    # TODO: Implement following the 5-step guidance above
    pass

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
        assert clone_node.val == 1
        assert clone_node.neighbors == None
    
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
        cloned_node1 = cloneGraph(node1)
        #   - Verify cloned node1 exists and has correct value
        assert cloned_node1 is not None
        #   - Verify cloned node1 is different object from original
        assert cloned_node1 is not node1
        #   - Verify cloned node1 has 2 neighbors
        assert len(cloned_node1.neighbors) == 2

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
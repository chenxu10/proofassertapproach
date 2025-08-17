import pytest
from collections import deque
from typing import List, Set, Dict, Any, Optional

def graph_dfs_template(input_data: Any, target: Any = None) -> Any:
    """
    Template for DFS-based graph problems
    Use for: connected components, path finding, graph cloning, cycle detection
    Examples: Number of Islands, Clone Graph, Valid Tree
    """
    # Step 1: Input validation and edge cases
    if not input_data:
        return None  # or appropriate default value
    
    # Step 2: Initialize data structures
    visited = set()  # or dict for more complex tracking
    result = 0  # or list, dict, etc. based on problem
    
    # Step 3: Define DFS helper function
    def dfs(current_node: Any) -> Any:
        # Base case: check bounds/validity and visited status
        if current_node in visited or not is_valid_node(current_node):
            return None  # or appropriate base case return
        
        # Mark as visited
        visited.add(current_node)
        
        # Process current node (problem-specific logic)
        local_result = process_node(current_node)
        
        # Recursive calls to neighbors
        neighbors = get_neighbors(current_node, input_data)
        for neighbor in neighbors:
            neighbor_result = dfs(neighbor)
            # Combine results if needed
            combine_results(local_result, neighbor_result)
        
        return local_result
    
    # Step 4: Main traversal loop (for disconnected components)
    start_nodes = get_start_nodes(input_data)
    for start_node in start_nodes:
        if start_node not in visited:
            component_result = dfs(start_node)
            # Accumulate results from each component
            result = accumulate_result(result, component_result)
    
    # Step 5: Return final result
    return result

def graph_bfs_template(start: Any, target: Any, input_data: Any) -> Any:
    """
    Template for BFS-based graph problems
    Use for: shortest path, level-order traversal, minimum steps
    Examples: Word Ladder, Shortest Path in Binary Matrix
    """
    # Step 1: Input validation and edge cases
    if not input_data or start == target:
        return get_default_result()
    
    # Step 2: Initialize BFS data structures
    queue = deque([(start, 0)])  # (node, distance/level)
    visited = set([start])
    
    # Step 3: BFS main loop
    while queue:
        current_node, distance = queue.popleft()
        
        # Check if target reached
        if is_target_reached(current_node, target):
            return distance + 1  # or appropriate result
        
        # Get and process neighbors
        neighbors = get_neighbors(current_node, input_data)
        for neighbor in neighbors:
            if neighbor not in visited and is_valid_neighbor(neighbor, input_data):
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    
    # Step 4: Return result if no path found
    return get_no_path_result()

def graph_adjacency_list_template(nodes: List[Any], edges: List[tuple]) -> Dict[Any, List[Any]]:
    """
    Template for building adjacency list representation
    Use for: graph construction from edge list
    """
    # Step 1: Initialize adjacency list
    adj_list = {node: [] for node in nodes}
    
    # Step 2: Add edges (undirected/directed based on problem)
    for edge in edges:
        if len(edge) == 2:
            node1, node2 = edge
            adj_list[node1].append(node2)
            # For undirected graphs:
            # adj_list[node2].append(node1)
    
    return adj_list

def graph_matrix_template(matrix: List[List[Any]], target_value: Any = '1') -> Any:
    """
    Template for matrix-based graph problems
    Use for: grid traversal, 2D path finding
    Examples: Number of Islands, Surrounded Regions
    """
    # Step 1: Input validation
    if not matrix or not matrix[0]:
        return get_default_result()
    
    # Step 2: Initialize dimensions and tracking
    rows, cols = len(matrix), len(matrix[0])
    visited = set()  # or 2D boolean matrix
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    result = 0
    
    # Step 3: Helper function to check valid coordinates
    def is_valid_cell(r: int, c: int) -> bool:
        return (0 <= r < rows and 0 <= c < cols and 
                (r, c) not in visited and 
                matrix[r][c] == target_value)
    
    # Step 4: DFS/BFS for each cell
    def traverse_component(start_r: int, start_c: int) -> Any:
        # Use DFS or BFS based on problem requirements
        stack = [(start_r, start_c)]  # or queue for BFS
        component_size = 0
        
        while stack:
            r, c = stack.pop()  # or popleft() for BFS
            
            if not is_valid_cell(r, c):
                continue
                
            visited.add((r, c))
            component_size += 1
            
            # Add neighbors to stack/queue
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if is_valid_cell(nr, nc):
                    stack.append((nr, nc))
        
        return component_size
    
    # Step 5: Main traversal loop
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited and matrix[r][c] == target_value:
                component_result = traverse_component(r, c)
                result = combine_component_results(result, component_result)
    
    return result

# Helper functions (implement based on specific problem)
def is_valid_node(node: Any) -> bool:
    """Check if node is valid for processing"""
    pass

def process_node(node: Any) -> Any:
    """Process current node and return local result"""
    pass

def get_neighbors(node: Any, input_data: Any) -> List[Any]:
    """Get list of neighboring nodes"""
    pass

def combine_results(local_result: Any, neighbor_result: Any) -> Any:
    """Combine results from current node and neighbors"""
    pass

def get_start_nodes(input_data: Any) -> List[Any]:
    """Get list of potential starting nodes"""
    pass

def accumulate_result(current_result: Any, component_result: Any) -> Any:
    """Accumulate results from multiple components"""
    pass

def get_default_result() -> Any:
    """Return default result for edge cases"""
    pass

def is_target_reached(current: Any, target: Any) -> bool:
    """Check if target is reached in BFS"""
    pass

def is_valid_neighbor(neighbor: Any, input_data: Any) -> bool:
    """Check if neighbor is valid for BFS expansion"""
    pass

def get_no_path_result() -> Any:
    """Return result when no path exists"""
    pass

def combine_component_results(current: Any, component: Any) -> Any:
    """Combine results from different components"""
    pass

class TestGraphTemplate:
    """Test cases demonstrating template usage"""
    
    def test_dfs_template_example(self):
        """Example usage of DFS template"""
        # This would be implemented for specific problems
        pass
    
    def test_bfs_template_example(self):
        """Example usage of BFS template"""
        # This would be implemented for specific problems
        pass
    
    def test_matrix_template_example(self):
        """Example usage of matrix template"""
        # This would be implemented for specific problems
        pass

if __name__ == "__main__":
    print("Graph Algorithm Templates")
    print("=" * 50)
    print("1. DFS Template - for connected components, path finding, cloning")
    print("2. BFS Template - for shortest paths, level traversal")
    print("3. Matrix Template - for 2D grid problems")
    print("4. Adjacency List Template - for graph construction")
    print("=" * 50)
    print("Customize helper functions based on specific problem requirements")
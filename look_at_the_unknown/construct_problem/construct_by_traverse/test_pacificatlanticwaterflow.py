import pytest


def pacificAtlantic(heights):
    """
    Find all cells where water can flow to both Pacific and Atlantic oceans.
    
    Args:
        heights (List[List[int]]): 2D grid representing island heights
        
    Returns:
        List[List[int]]: List of [row, col] coordinates where water can reach both oceans
    """
    if not heights or not heights[0]:
        return []
    
    m, n = len(heights), len(heights[0])
    pacific_visited = [[False] * n for _ in range(m)]
    atlantic_visited = [[False] * n for _ in range(m)]
    
    def dfs(i, j, visited, prev_height):
        if (i < 0 or i >= m or j < 0 or j >= n or 
            visited[i][j] or heights[i][j] < prev_height):
            return
        
        visited[i][j] = True
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for di, dj in directions:
            dfs(i + di, j + dj, visited, heights[i][j])
    
    # Start DFS from Pacific edges (top and left)
    for i in range(m):
        dfs(i, 0, pacific_visited, heights[i][0])
    for j in range(n):
        dfs(0, j, pacific_visited, heights[0][j])
    
    # Start DFS from Atlantic edges (bottom and right)
    for i in range(m):
        dfs(i, n-1, atlantic_visited, heights[i][n-1])
    for j in range(n):
        dfs(m-1, j, atlantic_visited, heights[m-1][j])
    
    # Find cells that can reach both oceans
    result = []
    for i in range(m):
        for j in range(n):
            if pacific_visited[i][j] and atlantic_visited[i][j]:
                result.append([i, j])
    
    return result



class TestPacificAtlanticWaterFlow:
    
    def test_basic_case(self):
        """Test basic case with water flowing to both oceans"""
        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4]
        ]
        result = pacificAtlantic(heights)
        expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        assert sorted(result) == sorted(expected)
    
    def test_single_cell(self):
        """Test single cell grid"""
        heights = [[1]]
        result = pacificAtlantic(heights)
        assert result == [[0, 0]]
    
    def test_single_row(self):
        """Test single row grid"""
        heights = [[2, 1]]
        result = pacificAtlantic(heights)
        expected = [[0, 0], [0, 1]]
        assert sorted(result) == sorted(expected)
    
    def test_single_column(self):
        """Test single column grid"""
        heights = [[2], [1]]
        result = pacificAtlantic(heights)
        expected = [[0, 0], [1, 0]]
        assert sorted(result) == sorted(expected)
    
    def test_no_flow_to_both(self):
        """Test case where no cell can reach both oceans"""
        heights = [
            [1, 1],
            [1, 1]
        ]
        result = pacificAtlantic(heights)
        expected = [[0, 0], [0, 1], [1, 0], [1, 1]]
        assert sorted(result) == sorted(expected)
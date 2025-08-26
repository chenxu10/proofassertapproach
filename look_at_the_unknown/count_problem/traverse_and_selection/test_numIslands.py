import pytest

def numIslands(grid):
    """
    Count the number of islands in a 2D grid.
    
    An island is surrounded by water ('0') and is formed by connecting 
    adjacent lands ('1') horizontally or vertically.
    
    This is a classic connected components problem in graph theory!
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
          
    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            (r, c) in visited or grid[r][c] == '0'):
            return
        
        visited.add((r, c))
        
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    
    def traverse_all_matrix(grid):
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        return islands

    islands = traverse_all_matrix(grid)
    return islands

class TestNumIslands:
    def test_example_1(self):
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        assert numIslands(grid) == 1
    
    def test_example_2(self):
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        assert numIslands(grid) == 3
    
    def test_single_island(self):
        grid = [["1"]]
        assert numIslands(grid) == 1
    
    def test_single_water(self):
        grid = [["0"]]
        assert numIslands(grid) == 0
    
    def test_all_water(self):
        grid = [
            ["0","0","0"],
            ["0","0","0"],
            ["0","0","0"]
        ]
        assert numIslands(grid) == 0
    
    def test_all_land(self):
        grid = [
            ["1","1","1"],
            ["1","1","1"],
            ["1","1","1"]
        ]
        assert numIslands(grid) == 1
    
    def test_diagonal_islands(self):
        grid = [
            ["1","0","1"],
            ["0","1","0"],
            ["1","0","1"]
        ]
        assert numIslands(grid) == 5
    
    def test_horizontal_line(self):
        grid = [["1","1","1","1","1"]]
        assert numIslands(grid) == 1
    
    def test_vertical_line(self):
        grid = [["1"], ["1"], ["1"], ["1"], ["1"]]
        assert numIslands(grid) == 1
    
    def test_empty_grid(self):
        grid = []
        assert numIslands(grid) == 0
    
    def test_empty_row(self):
        grid = [[]]
        assert numIslands(grid) == 0
    
    def test_alternating_pattern(self):
        grid = [
            ["1","0","1","0","1"],
            ["0","1","0","1","0"],
            ["1","0","1","0","1"]
        ]
        assert numIslands(grid) == 8
    
    def test_large_single_island(self):
        grid = [
            ["1","1","1","1","1"],
            ["1","0","0","0","1"],
            ["1","0","1","0","1"],
            ["1","0","0","0","1"],
            ["1","1","1","1","1"]
        ]
        assert numIslands(grid) == 2

if __name__ == "__main__":
    pytest.main([__file__])
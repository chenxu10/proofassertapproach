import pytest

def numIslands(grid):
    """
    Count the number of islands in a 2D grid.
    
    An island is surrounded by water ('0') and is formed by connecting 
    adjacent lands ('1') horizontally or vertically.
    
    This is a classic connected components problem in graph theory!
    """
    
    # HINT 1: Edge case handling - what should you return for invalid inputs?
    # Fill in: if not grid or not _____: return _____
    
    # HINT 2: Get grid dimensions for boundary checking
    # Fill in: rows, cols = _____, _____
    
    # HINT 3: What data structure tracks visited cells efficiently?
    # Fill in: visited = _____  # Think: set, list, or 2D boolean array?
    
    # HINT 4: Initialize counter for connected components (islands)
    # Fill in: islands = _____
    
    # HINT 5: Choose your traversal strategy
    # You can use DFS (recursive/iterative) or BFS. Which explores "deeper" first?
    # Implement your traversal function here:
    
    def dfs(r, c):
        # HINT 6: What are your base cases for recursion?
        # Check bounds: r < 0 or r >= _____ or c < 0 or c >= _____
        # Check if already visited: (r, c) in _____
        # Check if water: grid[r][c] == _____
        # Fill in: if (...): return
        
        # HINT 7: Mark current cell as visited
        # Fill in: visited._____(_____)
        
        # HINT 8: Explore all 4 adjacent directions
        # What are the 4 directions from cell (r,c)?
        # Fill in the recursive calls:
        # dfs(_____, _____)  # down
        # dfs(_____, _____)  # up  
        # dfs(_____, _____)  # right
        # dfs(_____, _____)  # left
        pass
    
    # HINT 9: Main algorithm - iterate through every cell
    # Fill in the nested loops:
    # for r in range(_____):
    #     for c in range(_____):
    
    # HINT 10: When do you start a new DFS?
    # You found an unvisited land cell - this starts a new island!
    # Fill in: if grid[r][c] == _____ and (r, c) not in _____:
    #     dfs(_____, _____)
    #     islands += _____
    
    # HINT 11: Return the total count
    # Fill in: return _____
    
    # BONUS CHALLENGES:
    # 1. Can you implement this using BFS instead? How would you modify the approach?
    # 2. Can you solve this using Union-Find (Disjoint Set Union)?
    # 3. What's the time and space complexity of your solution?
    # 4. How would you modify this to find the largest island?
    
    pass

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
        assert numIslands(grid) == 13
    
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
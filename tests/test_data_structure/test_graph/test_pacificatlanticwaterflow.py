import pytest


def pacificAtlantic(heights):
    """
    Find all cells where water can flow to both Pacific and Atlantic oceans.
    
    Args:
        heights (List[List[int]]): 2D grid representing island heights
        
    Returns:
        List[List[int]]: List of [row, col] coordinates where water can reach both oceans
    """
    # High level: for every element in matrix, dfs to see whether can hit both
    # atlantic and pacific
    # to simplify logic 
    # I will create helper function can hit atlantic and pacific
    # The backbone of algorithm should be similiar to number of islands



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
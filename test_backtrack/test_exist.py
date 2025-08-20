import unittest

def exist(board, word):
    """
    Given a 2D grid of characters board and a string word, return true if the word 
    is present in the grid, otherwise return false.
    
    For the word to be present it must be possible to form it with a path in the board 
    with horizontally or vertically neighboring cells. The same cell may not be used 
    more than once in a word.
    
    Call Pattern Example - backtrack(0,0,0) searching "ABC":
    
                    backtrack(0,0,0) 'A' (index=0)
                           │
                    ┌──────┼──────┐
                    │      │      │
              (1,0) 'S'  (0,1) 'B'  ...
                 │         │
                False   backtrack(0,1,1) 'B' (index=1)
                           │
                    ┌──────┼──────┐
                    │      │      │  
              (1,1) 'F'  (0,2) 'C'  ...
                 │         │
                False   backtrack(0,2,2) 'C' (index=2)
                           │
                    backtrack(0,3,3) (index=3)
                           │
                        return True
                    (index == len(word))

    Args:
        board: List[List[str]] - 2D grid of characters
        word: str - target word to search
        
    Returns:
        bool - True if word exists in board, False otherwise
    """
    if not board or not board[0] or not word:
        return False
    
    rows, cols = len(board), len(board[0])
    
    def backtrack(row, col, index):
        if index == len(word):
            return True
        
        if (row < 0 or row >= rows or col < 0 or col >= cols or 
            board[row][col] != word[index]):
            return False
        
        # Mark as visited
        temp = board[row][col]
        board[row][col] = '#'
        
        # Explore all 4 directions
        found = (backtrack(row + 1, col, index + 1) or
                backtrack(row - 1, col, index + 1) or
                backtrack(row, col + 1, index + 1) or
                backtrack(row, col - 1, index + 1))
        
        # Restore the cell
        board[row][col] = temp
        
        return found
    
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0] and backtrack(i, j, 0):
                return True
    
    return False


class TestWordSearch(unittest.TestCase):
    
    def test_word_exists_horizontal(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        word = "ABCCED"
        self.assertTrue(exist(board, word))
    
    def test_word_exists_vertical(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        word = "ASA"
        self.assertTrue(exist(board, word))
    
    def test_word_does_not_exist(self):
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        word = "ABCB"
        self.assertFalse(exist(board, word))
    
    def test_single_character_word(self):
        board = [
            ['A', 'B'],
            ['C', 'D']
        ]
        word = "A"
        self.assertTrue(exist(board, word))
    
    def test_empty_board(self):
        board = []
        word = "A"
        self.assertFalse(exist(board, word))


if __name__ == '__main__':
    unittest.main()
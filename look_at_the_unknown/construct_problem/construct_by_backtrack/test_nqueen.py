def solveNQueens(n):
    """
    Solve the N-Queens problem using backtracking.
    
    The N-Queens problem is to place N chess queens on an N×N chessboard 
    so that no two queens attack each other.
    
    Args:
        n (int): Size of the chessboard (N×N)
        
    Returns:
        List[List[str]]: All possible solutions where each solution is 
        represented as a list of strings, each string represents a row 
        of the chessboard with 'Q' for queen and '.' for empty space.
    """

    def valid_safety_of(board, row, col, n):
        """
        Check if placing a queen at board[row][col] is safe.
        
        Args:
            board (List[List[str]]): Current state of the board
            row (int): Row index to place queen
            col (int): Column index to place queen  
            n (int): Size of the board
            
        Returns:
            bool: True if placement is safe, False otherwise
        """
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 'Q':
                return False

        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == 'Q':
                return False
        return True

    def iterate_all_cols_by(board, row):
        for col in range(n):
            if valid_safety_of(board, row, col, n):
                board[row][col] = 'Q'
                backtrack(board, row + 1, col, n)
                board[row][col] = '.'

    def backtrack(board, row, col, solutions):
        # base case
        if row == n:
            solutions.append([''.join(row) for  row in board])
            return solutions
        else:
            iterate_all_cols_by(board, row)

    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    backtrack(board, 0, n, solutions)
    return solutions

class TestNQueens:
    def test_n_equals_2(self):
        """Test N-Queens for n=2 (impossible case)"""
        result = solveNQueens(2)
        expected = []
        assert result == expected, f"Expected {expected}, got {result}"
    
    def test_n_equals_3(self):
        """Test N-Queens for n=3 (impossible case)"""
        result = solveNQueens(3)
        expected = []
        assert result == expected, f"Expected {expected}, got {result}"
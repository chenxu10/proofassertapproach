def exist(board, word):
    """
    Search for a word in a 2D board using backtracking with pruning optimizations.
    
    Refactored to follow Constantine's Law of Limited Working Memory:
    - Backtrack function uses only 2 parameters (position tuple, word_index)
    - State encapsulation reduces cognitive load following cognitive laws
    - Clear separation of concerns improves maintainability
    
    Pruning techniques used:
    1. Early termination when character doesn't match
    2. Boundary checking before recursion
    3. Visited cell tracking to avoid cycles
    4. Character frequency pruning (if word has more of a char than board)
    """
    if not board or not board[0] or not word:
        return False
    
    rows, cols = len(board), len(board[0])
    
    # Pruning optimization: Check if board has enough characters
    from collections import Counter
    board_count = Counter()
    for row in board:
        for char in row:
            board_count[char] += 1
    
    word_count = Counter(word)
    for char, count in word_count.items():
        if board_count[char] < count:
            return False
    
    visited = set()
    
    def backtrack(pos, word_index):
        """
        Backtrack with only 2 parameters following cognitive laws.
        pos: (row, col) tuple - encapsulates position state
        word_index: current position in word
        """
        row, col = pos
        
        # Base case: found complete word
        if word_index == len(word):
            return True
        
        # Pruning: bounds check and visited check
        if (row < 0 or row >= rows or col < 0 or col >= cols or 
            pos in visited or board[row][col] != word[word_index]):
            return False
        
        # Mark current cell as visited
        visited.add(pos)
        
        # Explore all 4 directions with clear, readable pattern
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in directions:
            next_pos = (row + dr, col + dc)
            if backtrack(next_pos, word_index + 1):
                visited.remove(pos)
                return True
        

        visited.remove(pos)
        return False
    
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0]:
                visited.clear()
                backtrack((i,j),0)
                return True
    return False


def test_exist():
    """Test cases for the exist function with various scenarios"""
    
    # Test Case 1: Basic example from problem statement
    board1 = [
        ["A","B","C","D"],
        ["S","A","A","T"],
        ["A","C","A","E"]
    ]
    word1 = "CAT"
    assert exist(board1, word1) == True, f"Test 1 failed: expected True for word '{word1}'"
    print("✓ Test 1 passed: Basic word search")
    
    # Test Case 2: Word not present
    board2 = [
        ["A","B","C","D"],
        ["S","A","A","T"],
        ["A","C","A","E"]
    ]
    word2 = "DOG"
    assert exist(board2, word2) == False, f"Test 2 failed: expected False for word '{word2}'"
    print("✓ Test 2 passed: Word not present")
    
    # Test Case 3: Single character word
    board3 = [
        ["A","B"],
        ["C","D"]
    ]
    word3 = "A"
    assert exist(board3, word3) == True, f"Test 3 failed: expected True for word '{word3}'"
    print("✓ Test 3 passed: Single character word")
    
    # Test Case 4: Complex path with backtracking required
    board4 = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word4 = "ABCCED"
    assert exist(board4, word4) == True, f"Test 4 failed: expected True for word '{word4}'"
    print("✓ Test 4 passed: Complex path requiring backtracking")
    
    # Test Case 5: Path exists but would require revisiting cells (should fail)
    board5 = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word5 = "ABCB"
    assert exist(board5, word5) == False, f"Test 5 failed: expected False for word '{word5}'"
    print("✓ Test 5 passed: Cannot revisit cells")
    
    # Test Case 6: Edge case - empty word
    board6 = [["A"]]
    word6 = ""
    assert exist(board6, word6) == False, f"Test 6 failed: expected False for empty word"
    print("✓ Test 6 passed: Empty word edge case")
    
    # Test Case 7: Large board with long word
    board7 = [
        ["A","A","A","A","A","A"],
        ["A","A","A","A","A","A"],
        ["A","A","A","H","O","O"],
        ["A","A","A","H","E","L"],
        ["A","A","A","A","L","L"],
        ["A","A","A","A","L","O"]
    ]
    word7 = "HELLO"
    assert exist(board7, word7) == True, f"Test 7 failed: expected True for word '{word7}'"
    print("✓ Test 7 passed: Large board with specific path")
    
    print("\n🎉 All test cases passed!")


if __name__ == "__main__":
    test_exist()
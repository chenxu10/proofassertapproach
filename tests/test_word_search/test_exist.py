def exist(board, word):
    if not board or not board[0] or not word:
        return False
    
    rows, cols = len(board), len(board[0])
    
    # Character frequency pruning
    from collections import Counter
    board_chars = Counter(char for row in board for char in row)
    word_chars = Counter(word)
    if any(board_chars[char] < count for char, count in word_chars.items()):
        return False
    
    visited = set()
    
    def backtrack(r, c, i):
        if i == len(word):
            return True
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            (r, c) in visited or board[r][c] != word[i]):
            return False
        
        visited.add((r, c))
        found = any(backtrack(r + dr, c + dc, i + 1) 
                   for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)])
        visited.remove((r, c))
        return found
    
    return any(backtrack(i, j, 0) for i in range(rows) for j in range(cols) 
              if board[i][j] == word[0])


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
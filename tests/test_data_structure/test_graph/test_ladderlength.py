import pytest
from collections import deque

def ladderLength(beginWord, endWord, wordList):
    """
    Word Ladder Problem - Find shortest transformation sequence
    
    🎯 LEARNING OBJECTIVE: Practice BFS for shortest path in unweighted graphs
    
    💡 HINTS TO GET YOU STARTED:
    
    1. GRAPH REPRESENTATION: Think of this as a graph problem where:
       - Each word is a node
       - Two words are connected if they differ by exactly one character
       - We need the shortest path from beginWord to endWord
    
    2. ALGORITHM CHOICE: Which graph algorithm finds shortest paths?
       - DFS finds A path, but not necessarily the shortest
       - BFS finds the shortest path in unweighted graphs ✓
    
    3. EARLY TERMINATION: What simple check can save us time?
       - If endWord isn't in wordList, what should we return?
    
    4. DATA STRUCTURES TO CONSIDER:
       - Queue for BFS traversal (what should each queue element contain?)
       - Set for O(1) lookup of valid words
       - Set to track visited words (why is this important?)
    
    5. GENERATING NEIGHBORS: For each word, how do we find all valid neighbors?
       - Try changing each position to every letter a-z
       - Check if the new word exists in our word set
       - Make sure we haven't visited it before
    
    6. TRACKING DISTANCE: How do we know the length of the transformation?
       - Store distance with each word in the queue, OR
       - Process level by level and increment counter
    
    ⚠️ COMMON PITFALLS:
    - Forgetting to mark words as visited when adding to queue (not when processing)
    - Not handling the case where endWord is not in wordList
    - Starting distance from 0 instead of 1
    
    🔍 TEST YOUR UNDERSTANDING:
    - Why BFS instead of DFS?
    - Why do we need a visited set?
    - When should we mark a word as visited?
    """
    steps = 0
    # TODO: Implement your solution here
    # Start with the base case checks
    # Then set up your BFS data structures
    # Finally implement the main BFS loop


    queue = deque([(beginWord, 1)])
    visited = set([beginWord])

    while queue:
        word, step = queue.popleft()
        if word == endWord:
            return step
        
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + c + word[i+1:]
                if new_word not in visited and new_word in wordList:
                    queue.append((new_word, step + 1))
                    visited.add(new_word)
    
    return 0

class TestLadderLength:
    def test_example_1(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        assert ladderLength(beginWord, endWord, wordList) == 5
    
    def test_example_2(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]
        assert ladderLength(beginWord, endWord, wordList) == 0
    
    def test_single_step(self):
        beginWord = "cat"
        endWord = "bat"
        wordList = ["bat"]
        assert ladderLength(beginWord, endWord, wordList) == 2
    
    def test_same_word(self):
        beginWord = "cat"
        endWord = "cat"
        wordList = ["cat"]
        assert ladderLength(beginWord, endWord, wordList) == 1
    
    def test_direct_transformation(self):
        beginWord = "a"
        endWord = "c"
        wordList = ["a","b","c"]
        assert ladderLength(beginWord, endWord, wordList) == 2
    
    def test_no_path_exists(self):
        beginWord = "abc"
        endWord = "xyz"
        wordList = ["def","ghi","jkl"]
        assert ladderLength(beginWord, endWord, wordList) == 0
    
    def test_endword_not_in_wordlist(self):
        beginWord = "cat"
        endWord = "dog"
        wordList = ["bat","rat","hat"]
        assert ladderLength(beginWord, endWord, wordList) == 0
    
    def test_empty_wordlist(self):
        beginWord = "cat"
        endWord = "dog"
        wordList = []
        assert ladderLength(beginWord, endWord, wordList) == 0
    
    def test_longer_path(self):
        beginWord = "hot"
        endWord = "dog"
        wordList = ["hot","dot","dog"]
        assert ladderLength(beginWord, endWord, wordList) == 3
    
    def test_multiple_paths(self):
        beginWord = "red"
        endWord = "tax"
        wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
        assert ladderLength(beginWord, endWord, wordList) == 4
    
    def test_single_character_words(self):
        beginWord = "a"
        endWord = "z"
        wordList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        assert ladderLength(beginWord, endWord, wordList) == 2
    
    def test_circular_path(self):
        beginWord = "cat"
        endWord = "dog"
        wordList = ["bat","bag","dag","dog"]
        assert ladderLength(beginWord, endWord, wordList) == 5
    
    def test_isolated_word(self):
        beginWord = "abc"
        endWord = "def"
        wordList = ["abc","def","xyz"]
        assert ladderLength(beginWord, endWord, wordList) == 0
    
    def test_begin_word_in_wordlist(self):
        beginWord = "cat"
        endWord = "dog"
        wordList = ["cat","bat","bag","dag","dog"]
        assert ladderLength(beginWord, endWord, wordList) == 5
    
    def test_all_same_except_one(self):
        beginWord = "aaaa"
        endWord = "aaab"
        wordList = ["aaaa","aaab"]
        assert ladderLength(beginWord, endWord, wordList) == 2
    
    def test_long_transformation(self):
        beginWord = "game"
        endWord = "thee"
        wordList = ["game","gate","gave","have","hate","date","late","make","take","thee"]
        result = ladderLength(beginWord, endWord, wordList)
        assert result > 0

if __name__ == "__main__":
    pass
import pytest
from collections import deque

def ladderLength(beginWord, endWord, wordList):
    queue = deque([(beginWord, 1)])
    visited = set([beginWord])

    def generate_neighbors(word):
        neighbors = []
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + c + word[i+1:]
                neighbors.append(new_word)
        return neighbors
    
    while queue:
        word, step = queue.popleft()
        if word == endWord:
            return step
        
        neighbors = generate_neighbors(word)    
        for n in neighbors:
            if n not in visited and n in wordList:
                queue.append((n, step + 1))
                visited.add(n)
    
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
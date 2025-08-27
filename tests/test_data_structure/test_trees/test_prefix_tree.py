import pytest


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """
    Implement a Trie (Prefix Tree) data structure.
    
    A trie is a tree-like data structure that stores a dynamic set of strings,
    usually used for efficient retrieval of a key in a dataset of strings.
    """
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """
        Inserts a word into the trie.
        
        Args:
            word (str): The word to insert
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        """
        Returns True if word is in the trie.
        
        Args:
            word (str): The word to search for
            
        Returns:
            bool: True if word exists in trie, False otherwise
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def startsWith(self, prefix):
        """
        Returns True if there is a previously inserted string word that has the prefix.
        
        Args:
            prefix (str): The prefix to search for
            
        Returns:
            bool: True if prefix exists, False otherwise
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


class TestTrie:
    
    def test_basic_operations(self):
        """Test basic insert, search, and startsWith operations"""
        trie = Trie()
        
        # Insert words
        trie.insert("apple")
        assert trie.search("apple") == True
        assert trie.search("app") == False
        assert trie.startsWith("app") == True
        
        trie.insert("app")
        assert trie.search("app") == True
    
    def test_empty_trie(self):
        """Test operations on empty trie"""
        trie = Trie()
        assert trie.search("anything") == False
        assert trie.startsWith("any") == False
    
    def test_single_character(self):
        """Test single character words"""
        trie = Trie()
        trie.insert("a")
        assert trie.search("a") == True
        assert trie.search("ab") == False
        assert trie.startsWith("a") == True
    
    def test_overlapping_words(self):
        """Test words that are prefixes of other words"""
        trie = Trie()
        words = ["cat", "cats", "caterpillar", "car", "card"]
        
        for word in words:
            trie.insert(word)
        
        # All inserted words should be found
        for word in words:
            assert trie.search(word) == True
        
        # Test prefixes
        assert trie.startsWith("cat") == True
        assert trie.startsWith("ca") == True
        assert trie.startsWith("c") == True
        
        # Test non-existing words
        assert trie.search("ca") == False
        assert trie.search("cater") == False
    
    def test_case_sensitivity(self):
        """Test that trie is case sensitive"""
        trie = Trie()
        trie.insert("Apple")
        
        assert trie.search("Apple") == True
        assert trie.search("apple") == False
        assert trie.startsWith("App") == True
        assert trie.startsWith("app") == False
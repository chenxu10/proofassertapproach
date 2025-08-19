import pytest

def word_break(s, word_dict):
    """
    Given a string s and a dictionary of strings wordDict, return true if s 
    can be segmented into a space-separated sequence of dictionary words.
    
    Args:
        s: string to be segmented
        word_dict: list of dictionary words
    
    Returns:
        bool: True if s can be segmented, False otherwise

    ["apple","pen","ape"]
     wordBreak("applepenapple")
                         |
                Try all prefixes
                    /    |    \
              "a" ✗   "ap" ✗   "app" ✗
                         |
                    "appl" ✗
                         |
                    "apple" ✓
                         |
                wordBreak("penapple")
                         |
                    Try prefixes
                      /   |   \
                 "p" ✗  "pe" ✗  "pen" ✓
                              |
                         wordBreak("apple")
                              |
                         "apple" ✓
                              |
                         wordBreak("") = True
    """
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True 
    word_set = set(word_dict)

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    # if dp[j] and s[j:i] dp[i] = True
    return dp[n]

class TestWordBreak:
    def test_basic_segmentation(self):
        """Test basic word segmentation"""
        s = "leetcode"
        word_dict = ["leet", "code"]
        assert word_break(s, word_dict) == True
    
    def test_reuse_dictionary_words(self):
        """
        🤔 Think: Can dictionary words be reused multiple times?
        
        💡 Hint: Consider a string like "applepenapple" with dict ["apple", "pen"]
        🧠 Mental trace: What happens at each dp[i] when we find "apple" twice?
        🎯 Key insight: Why does dynamic programming naturally handle word reuse?
        
        ✏️ Your task: Design a test case and mentally verify the result
        """
        # TODO: Write your test case here - think about word reuse patterns
        assert word_break("applepenapple",["apple","pen"]) == True
    
    def test_impossible_segmentation(self):
        """Test case where segmentation is impossible"""
        s = "catsandog"
        word_dict = ["cats", "dog", "sand", "and", "cat"]
        assert word_break(s, word_dict) == False
    
    def test_single_word_match(self):
        """
        🎯 Simple case: What if the entire string is one dictionary word?
        
        💡 Hint: Consider "python" with dictionary ["python", "java", "code"]
        🤔 Think: How many iterations does the DP algorithm need?
        📊 Trace: What values will dp[0] through dp[6] contain?
        
        ⚡ Efficiency note: This is the best-case scenario - why?
        
        ✏️ Your task: Create this test and predict the dp array contents
        """
        # TODO: Implement this straightforward case and verify your prediction
        assert word_break("python",["python","java"]) == True
    
    def test_empty_string(self):
        """Test empty string"""
        s = ""
        word_dict = ["a", "b"]
        assert word_break(s, word_dict) == True
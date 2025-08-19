import pytest

def word_break(s, word_dict):
    """
    🎯 Challenge: Implement word segmentation using dynamic programming
    
    Given a string s and a dictionary of strings wordDict, return true if s 
    can be segmented into a space-separated sequence of dictionary words.
    
    💡 Key insights to guide your thinking:
    
    🧠 DP State Design:
    - What does dp[i] represent? (Think: "Can we segment s[0:i]?")
    - What's your base case? (Hint: empty string is always segmentable)
    
    🔍 Transition Logic:
    - For position i, what smaller subproblems do you check?
    - If dp[j] is True and s[j:i] is in dictionary, what can you conclude?
    
    ⚡ Optimization Tips:
    - Convert word_dict to set for O(1) lookups
    - Use break once you find a valid segmentation for position i
    
    📊 Trace through "leetcode" with ["leet", "code"]:
    - dp[0] = True (base case)
    - dp[4] = ? (check if "leet" in dict and dp[0] is True)
    - dp[8] = ? (check if "code" in dict and dp[4] is True)
    
    🎮 Your mission: Fill in the implementation below!
    """
    # Step 1: Setup - what variables do you need?
    # n = ?
    # dp = ?
    # word_set = ?
    n = len(s)
    dp = [False] * (n + 1)
    word_set = set(word_dict)
    
    # Step 2: Base case - what should dp[0] be?
    if s == "":
        dp[0] = True
    
    else:
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_dict:
                    return True
                else:
                    return False
                
    return dp[n -1]
    # Step 3: Fill the DP table
    # for i in range(...):
    #     for j in range(...):
    #         # Check: if we can reach j AND s[j:i] is a valid word
    #         if ... and ... in ...:
    #             # Then we can reach position i
    #             dp[i] = ...
    #             break  # Early termination - why is this helpful?
    
    # Step 4: Return the answer
    # return dp[?]
    
    # TODO: Replace this placeholder with your implementation
    pass

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
import unittest

def longestCommonSubsequence(text1: str, text2: str) -> int:
    """
    Find the length of longest common subsequence between two strings using 2D DP.
    
    Data Flow Diagram (Example: text1="abcde", text2="ace"):
    
    Input Processing:
    text1 = "abcde" (m=5)  →  indices: 0:'a', 1:'b', 2:'c', 3:'d', 4:'e'
    text2 = "ace"   (n=3)  →  indices: 0:'a', 1:'c', 2:'e'
    
    DP Table Construction (dp[i][j] = LCS length for text1[0:i] and text2[0:j]):
    
         ""  a   c   e     ← text2 characters
    ""   0   0   0   0     ← Base case: empty string
    a    0   1   1   1     ← text1[0]='a' matches text2[0]='a'
    b    0   1   1   1     ← text1[1]='b' no match, inherit max
    c    0   1   2   2     ← text1[2]='c' matches text2[1]='c'
    d    0   1   2   2     ← text1[3]='d' no match, inherit max
    e    0   1   2   3     ← text1[4]='e' matches text2[2]='e'
    ↑
    text1 chars
    
    Recurrence Relation:
    if text1[i-1] == text2[j-1]:  dp[i][j] = dp[i-1][j-1] + 1  (diagonal + 1)
    else:                         dp[i][j] = max(dp[i-1][j], dp[i][j-1])  (max of top/left)
    
    Data Flow:
    Input → Character comparison → DP table fill → Return dp[m][n]
    Result: LCS("abcde", "ace") = 3 (subsequence: "ace")
    """
    m = len(text1)
    n = len(text2)

    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]     

class TestLongestCommonSubsequence(unittest.TestCase):
    
    def test_basic_case(self):
        self.assertEqual(longestCommonSubsequence("abcde", "ace"), 3)
        self.assertEqual(longestCommonSubsequence("abc", "abc"), 3)
    
    def test_empty_strings(self):
        self.assertEqual(longestCommonSubsequence("", ""), 0)
        self.assertEqual(longestCommonSubsequence("abc", ""), 0)
        self.assertEqual(longestCommonSubsequence("", "abc"), 0)
    
    def test_no_common_subsequence(self):
        self.assertEqual(longestCommonSubsequence("abc", "def"), 0)
    
    def test_identical_strings(self):
        self.assertEqual(longestCommonSubsequence("test", "test"), 4)
    
    def test_one_char_strings(self):
        self.assertEqual(longestCommonSubsequence("a", "a"), 1)
        self.assertEqual(longestCommonSubsequence("a", "b"), 0)


if __name__ == '__main__':
    unittest.main()
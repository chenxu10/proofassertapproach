import unittest

class Solution:
    def lengthOfLIS(self, nums):
        """
        Find the length of the longest strictly increasing subsequence.
        
        Key insights for students to remember:
        1. DP state: dp[i] = length of LIS ending at index i
        2. For each position, consider all previous elements that are smaller
        3. Take the maximum LIS length from valid previous positions and add 1
        
        ASCII Diagram - Data Flow:
        nums:  [10, 9, 2, 5, 3, 7, 101, 18]
        dp:    [ 1, 1, 1, 2, 2, 3,  4,   4]
               
        Flow for dp[5] (value 7):
        - Check nums[0]=10 > 7? No, skip
        - Check nums[1]=9 > 7? No, skip  
        - Check nums[2]=2 < 7? Yes, dp[5] = max(dp[5], dp[2]+1) = max(1, 2)
        - Check nums[3]=5 < 7? Yes, dp[5] = max(dp[5], dp[3]+1) = max(2, 3)
        - Check nums[4]=3 < 7? Yes, dp[5] = max(dp[5], dp[4]+1) = max(3, 3)
        - Final: dp[5] = 3
        
        Time: O(n²), Space: O(n)
        """
        if not nums:
            return 0
            
        # TODO: Initialize DP array where dp[i] represents ___________
        dp = [1] * len(nums)  # Hint: What's the minimum LIS length ending at any position?
        
        # TODO: Fill the DP array
        for i in range(1, len(nums)):  # Hint: Start from which index?
            for j in range(i):  # Hint: Check which previous elements?
                if nums[i] > nums[j]:  # Hint: When can we extend a subsequence?
                    dp[i] = max(dp[i], dp[j] + 1)  # Hint: How to update current position?
        
        # TODO: Return the maximum value from DP array
        return max(dp)  # Hint: Why do we need max() here?

class TestLengthOfLIS(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_basic_increasing_sequence(self):
        """Test with basic increasing subsequence"""
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        expected = 4  # [2, 3, 7, 101] or [2, 3, 7, 18]
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)
    
    def test_all_decreasing(self):
        """Test with strictly decreasing sequence"""
        nums = [7, 7, 7, 7, 7, 7, 7]
        expected = 1  # Any single element
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)
    
    def test_single_element(self):
        """Test with single element"""
        nums = [1]
        expected = 1
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)
    
    def test_strictly_increasing(self):
        """Test with already sorted increasing sequence"""
        nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
        expected = 6  # [1, 3, 6, 7, 9, 10]
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)
    
    def test_mixed_pattern(self):
        """Test with complex mixed pattern"""
        nums = [0, 1, 0, 3, 2, 3]
        expected = 4  # [0, 1, 2, 3]
        self.assertEqual(self.solution.lengthOfLIS(nums), expected)

if __name__ == '__main__':
    unittest.main()
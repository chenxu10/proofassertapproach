import pytest
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Find the subarray with the largest sum using Kadane's algorithm.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Args:
            nums: List of integers
            
        Returns:
            Maximum sum of any contiguous subarray
        """
        if not nums:
            return 0
        
        max_sum = nums[0]
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        
        return max_sum


class TestMaxSubArray:
    def test_single_element(self):
        solution = Solution()
        assert solution.maxSubArray([5]) == 5
        assert solution.maxSubArray([-1]) == -1

    def test_all_negative(self):
        solution = Solution()
        assert solution.maxSubArray([-2, -3, -1, -5]) == -1

    def test_mixed_numbers(self):
        solution = Solution()
        assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    def test_all_positive(self):
        solution = Solution()
        assert solution.maxSubArray([1, 2, 3, 4, 5]) == 15

    def test_leetcode_example(self):
        solution = Solution()
        assert solution.maxSubArray([5, 4, -1, 7, 8]) == 23
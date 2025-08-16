import pytest

def longest_increasing_subsequence(nums):
    """
    Given an integer array nums, return the length of the longest strictly 
    increasing subsequence.
    
    A subsequence is a sequence that can be derived from the given sequence 
    by deleting some or no elements without changing the relative order of 
    the remaining elements.
    
    Args:
        nums: list of integers
    
    Returns:
        int: length of the longest strictly increasing subsequence
    
    Example: nums = [10,9,2,5,3,7,101,18]
    
                    LIS([10,9,2,5,3,7,101,18])
                               |
                        For each element, decide:
                        include it or skip it
                           /              \
                    Include 10         Skip 10
                   LIS([9,2,5,3,7,101,18])  LIS([9,2,5,3,7,101,18])
                      (last=10)              (last=inf)
                         |                      |
                    Skip 9 (9<10)         Include 9
                 LIS([2,5,3,7,101,18])  LIS([2,5,3,7,101,18])
                    (last=10)              (last=9)
                         |                   /        \
                    Skip 2 (2<10)     Include 2      Skip 2
                LIS([5,3,7,101,18])  LIS([5,3,7,101,18]) LIS([5,3,7,101,18])
                   (last=10)            (last=2)          (last=9)
                                           |
                                     Include 5 (5>2)
                                  LIS([3,7,101,18])
                                      (last=5)
                                          |
                                     Skip 3 (3<5)
                                  LIS([7,101,18])
                                      (last=5)
                                          |
                                     Include 7 (7>5)
                                  LIS([101,18])
                                      (last=7)
                                          |
                                     Include 101 (101>7)
                                    LIS([18])
                                     (last=101)
                                          |
                                     Skip 18 (18<101)
                                       LIS([])
                                     (last=101)
                                          |
                                      return 0
                                          
    Final LIS: [2,5,7,101] with length 4
    """
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

class TestLongestIncreasingSubsequence:
    def test_standard_case(self):
        """Test with standard mixed array"""
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        assert longest_increasing_subsequence(nums) == 4
    
    def test_strictly_increasing(self):
        """Test with already strictly increasing array"""
        nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
        assert longest_increasing_subsequence(nums) == 6
    
    def test_strictly_decreasing(self):
        """Test with strictly decreasing array"""
        nums = [7, 7, 7, 7, 7, 7, 7]
        assert longest_increasing_subsequence(nums) == 1
    
    def test_single_element(self):
        """Test with single element array"""
        nums = [42]
        assert longest_increasing_subsequence(nums) == 1
    
    def test_empty_array(self):
        """Test with empty array"""
        nums = []
        assert longest_increasing_subsequence(nums) == 0
import unittest
from typing import List

def maxProduct(nums: List[int]) -> int:
    # not nums return None
    # n = len(nums)
    # dp = [None] * n
    # dp[0] = nums[0]
    # return nums[0]

    # dp[i] the largest product up until i
    # max_ending at current postion min_ending at curren position

    # transition function max(dp[i], dp[i] * nums[i - 1])
    # return max(dp)


    # [-3 2] [2] [-6]
    if not nums:
        return 0
    
    global_max = nums[0]
    cur_min = nums[0]
    cur_max = nums[0]

    # iterate through nums
    for i in range(1, len(nums)):
        # update cur_max
        temp_max = max(nums[i], nums[i] * cur_max, nums[i] * cur_min)
        # update cur_min
        cur_min = min(nums[i], nums[i] * cur_max, nums[i] * cur_min)
        cur_max = temp_max

        global_max = max(global_max, cur_max)
        # update global

    return global_max

class TestMaxProduct(unittest.TestCase):
    
    def test_basic_positive_array(self):
        pass
    
    def test_array_with_negative_numbers(self):
        pass
    
    def test_array_with_zero(self):
        pass
    
    def test_single_element(self):
        pass
    
    def test_alternating_positive_negative(self):
        pass


if __name__ == "__main__":
    unittest.main()
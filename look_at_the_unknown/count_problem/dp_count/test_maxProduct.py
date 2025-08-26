import unittest
from typing import List

def maxProduct(nums: List[int]) -> int:
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
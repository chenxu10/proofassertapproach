import pytest


def findMin(nums):
    """
    Find the minimum element in a rotated sorted array.
    
    Algorithm: Binary Search
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    Proof of O(log n) complexity:
    - We use binary search, which divides the search space in half at each step
    - In each iteration, we eliminate half of the remaining elements
    - Starting with n elements, after k iterations we have n/2^k elements
    - We stop when we have 1 element, so n/2^k = 1, which gives k = log2(n)
    - Therefore, time complexity is O(log n)
    
    Algorithm correctness proof:
    - The array is originally sorted, then rotated at some pivot point
    - This creates two sorted subarrays: [pivot...end] and [start...pivot-1]
    - The minimum element is always at the start of the first subarray (at pivot)
    - At each step, we compare mid with right:
      * If nums[mid] > nums[right]: minimum is in right half (mid+1 to right)
      * If nums[mid] < nums[right]: minimum is in left half (left to mid)
      * We never miss the minimum because we always keep the half containing it
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left]


class TestFindMin:
    def test_single_element(self):
        """Test array with single element"""
        assert findMin([1]) == 1
    
    def test_two_elements_rotated(self):
        """Test array with two elements, rotated"""
        assert findMin([2, 1]) == 1
    
    def test_two_elements_not_rotated(self):
        """Test array with two elements, not rotated"""
        assert findMin([1, 2]) == 1
    
    def test_not_rotated_array(self):
        """Test array that is not rotated (rotation point is 0)"""
        assert findMin([1, 2, 3, 4, 5]) == 1
    
    def test_rotated_at_end(self):
        """Test array rotated at the last position"""
        assert findMin([2, 3, 4, 5, 1]) == 1
    
    def test_rotated_in_middle(self):
        """Test array rotated in the middle"""
        assert findMin([3, 4, 5, 1, 2]) == 1
        assert findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    
    def test_rotated_at_beginning(self):
        """Test array rotated near the beginning"""
        assert findMin([5, 1, 2, 3, 4]) == 1
    
    def test_larger_arrays(self):
        """Test with larger arrays"""
        assert findMin([6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 1
        assert findMin([10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
    
    def test_negative_numbers(self):
        """Test arrays containing negative numbers"""
        assert findMin([-1, 0, 1, 2, -2]) == -2
        assert findMin([3, 4, 5, -1, 0, 1, 2]) == -1
    
    def test_all_same_elements_except_one(self):
        """Test edge case with mostly duplicate elements"""
        assert findMin([1, 1, 1, 0, 1]) == 0
        assert findMin([1, 0, 1, 1, 1]) == 0


def test_complexity_verification():
    """
    Verification that the algorithm maintains O(log n) complexity.
    
    This test doesn't run the algorithm but serves as documentation
    of the complexity analysis:
    
    Mathematical Proof:
    1. Binary search reduces search space by half each iteration
    2. T(n) = T(n/2) + O(1)
    3. By Master Theorem: T(n) = O(log n)
    
    Empirical verification would show:
    - Array size 1000 → ~10 operations
    - Array size 1,000,000 → ~20 operations  
    - Array size 1,000,000,000 → ~30 operations
    
    Space complexity: O(1) - only using constant extra variables (left, right, mid)
    """
    pass


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
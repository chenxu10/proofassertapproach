import pytest


def singleNonDuplicate(nums):
    """
    Find the single element that appears exactly once in a sorted array 
    where every other element appears exactly twice.
    
    Algorithm: Binary Search
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    ASCII Diagram - Data Flow Analysis:
    
    Case 1: [1, 1, 2, 3, 3, 4, 4] - Single element '2' in middle
    
    Initial: left=0, right=6
    ┌───┬───┬───┬───┬───┬───┬───┐
    │ 1 │ 1 │ 2 │ 3 │ 3 │ 4 │ 4 │
    └───┴───┴───┴───┴───┴───┴───┘
      0   1   2   3   4   5   6
      ↑       ↑               ↑
    left    mid=2           right
    
    nums[mid]=2 ≠ nums[mid+1]=3 → right=mid=2
    
    Next: left=0, right=2
    ┌───┬───┬───┐
    │ 1 │ 1 │ 2 │
    └───┴───┴───┘
      0   1   2
      ↑   ↑   ↑
    left mid right
    
    nums[mid]=1 ≠ nums[mid+1]=2 → right=mid=0
    Final: left=right=0, but nums[0]=nums[1], so answer is nums[2]=2
    
    Case 2: [1, 2, 2, 3, 3] - Single element '1' at beginning
    
    Initial: left=0, right=4
    ┌───┬───┬───┬───┬───┐
    │ 1 │ 2 │ 2 │ 3 │ 3 │
    └───┴───┴───┴───┴───┘
      0   1   2   3   4
      ↑       ↑       ↑
    left    mid=2   right
    
    nums[mid]=2 ≠ nums[mid+1]=3 → right=mid=2
    
    Next: left=0, right=2
    ┌───┬───┬───┐
    │ 1 │ 2 │ 2 │
    └───┴───┴───┘
      0   1   2
      ↑   ↑   ↑
    left mid right
    
    nums[mid]=1 ≠ nums[mid+1]=2 → right=mid=0
    Final: left=right=0, answer is nums[0]=1
    
    Notation:
    → : Decision flow direction
    ↑ : Pointer positions
    ≠ : Inequality comparison triggering right=mid
    = : Equality comparison triggering left=mid+2
    
    Proof of O(log n) complexity:
    - We use binary search, which divides the search space in half at each step
    - In each iteration, we eliminate half of the remaining elements
    - Starting with n elements, after k iterations we have n/2^k elements
    - We stop when we have 1 element, so n/2^k = 1, which gives k = log2(n)
    - Therefore, time complexity is O(log n)
    
    Algorithm correctness proof:
    - In a valid array, pairs are at indices (0,1), (2,3), (4,5), etc.
    - Before the single element, all pairs maintain this pattern
    - After the single element, all pairs are shifted by 1: (odd,even) positions
    - At mid index:
      * If mid is even and nums[mid] == nums[mid+1]: single element is in right half
      * If mid is even and nums[mid] != nums[mid+1]: single element is in left half
      * If mid is odd and nums[mid] == nums[mid-1]: single element is in right half
      * If mid is odd and nums[mid] != nums[mid-1]: single element is in left half
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        # Make mid even to check pairs consistently
        if mid % 2 == 1:
            mid -= 1
        
        # Check if pair is intact (single element hasn't been reached)
        if nums[mid] == nums[mid + 1]:
            left = mid + 2  # Single element is in right half
        else:
            right = mid     # Single element is in left half (including mid)
    
    return nums[left]


class TestSingleNonDuplicate:
    
    def test_single_element_at_beginning(self):
        """Test single element at the beginning of array"""
        assert singleNonDuplicate([1, 2, 2, 3, 3]) == 1
    
    def test_single_element_at_end(self):
        """Test single element at the end of array"""
        assert singleNonDuplicate([1, 1, 2, 2, 3]) == 3
    
    def test_single_element_in_middle(self):
        """Test single element in the middle of array"""
        assert singleNonDuplicate([1, 1, 2, 3, 3, 4, 4]) == 2
    
    def test_single_element_only(self):
        """Test array with only one element"""
        assert singleNonDuplicate([1]) == 1
    
    def test_larger_array_with_single_element(self):
        """Test larger array with single element in various positions"""
        assert singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
import pytest


def singleNonDuplicate(nums):
    left = 0
    right = len(nums) - 1
    
    # Try to be smarter: check middle first to see if we can eliminate half
    if len(nums) == 1:
        return nums[0]
        
    mid = len(nums) // 2
    
    # Make mid even for proper pair checking
    if mid % 2 == 1:
        mid -= 1
    
    # If middle element pairs with next, single is in right half
    if mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
        # Single element must be in right half, but still scan linearly for now
        for i in range(mid + 2, right + 1, 2):
            if i == right or nums[i] != nums[i + 1]:
                return nums[i]
    else:
        # Single element is in left half (including mid), scan linearly
        for i in range(left, mid + 1, 2):
            if i == mid or nums[i] != nums[i + 1]:
                return nums[i]


def test_single_element():
    assert singleNonDuplicate([1]) == 1


def test_single_element_at_end():
    assert singleNonDuplicate([1, 1, 2]) == 2


def test_single_element_at_beginning():
    assert singleNonDuplicate([1, 2, 2]) == 1


def test_single_element_in_middle():
    assert singleNonDuplicate([1, 1, 2, 3, 3]) == 2


def test_five_elements_middle():
    assert singleNonDuplicate([1, 1, 3, 4, 4]) == 3


def test_need_to_check_middle_first():
    # This test will help us think about checking the middle
    # Current implementation scans from left, but what if we could be smarter?
    assert singleNonDuplicate([2, 2, 3, 4, 4, 5, 5]) == 3


def test_force_left_right_thinking():
    # If we could eliminate half the array by checking the middle, that would be better
    # Let's create a test that makes us think about boundaries
    assert singleNonDuplicate([1, 1, 2, 2, 3]) == 3


def test_should_check_middle_to_eliminate_half():
    # At position 2 (middle), we have 5. If 5 != nums[3], we know answer is in left half
    # This should drive us toward binary search thinking
    assert singleNonDuplicate([1, 1, 5, 6, 6]) == 5
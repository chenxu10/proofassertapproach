import pytest


def singleNonDuplicate(nums):
    left = 0
    right = len(nums) - 1
    
    # Still using linear approach but with left/right thinking
    for i in range(left, right + 1, 2):
        if i == right or nums[i] != nums[i + 1]:
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
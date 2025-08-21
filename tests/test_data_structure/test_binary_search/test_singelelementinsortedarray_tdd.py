import pytest


def singleNonDuplicate(nums):
    for i in range(0, len(nums), 2):
        if i == len(nums) - 1 or nums[i] != nums[i + 1]:
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
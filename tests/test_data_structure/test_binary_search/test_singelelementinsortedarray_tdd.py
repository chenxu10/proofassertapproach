import pytest


def singleNonDuplicate(nums):
    for i in range(0, len(nums), 2):
        if i == len(nums) - 1 or nums[i] != nums[i + 1]:
            return nums[i]


def test_single_element():
    assert singleNonDuplicate([1]) == 1


def test_single_element_at_end():
    assert singleNonDuplicate([1, 1, 2]) == 2
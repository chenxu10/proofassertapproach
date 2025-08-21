import pytest


def singleNonDuplicate(nums):
    return nums[0]


def test_single_element():
    assert singleNonDuplicate([1]) == 1
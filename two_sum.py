"""
Two Sum Algorithm Implementation
Following the constructive proof approach from plan.md

Problem: Given an array of integers and a target sum, 
find two numbers that add up to the target.

This implementation uses a hash map approach for O(n) time complexity
while maintaining correctness properties verified by the test cases.
"""


def two_sum(nums, target):
    """
    Find two numbers in nums that add up to target.
    
    Args:
        nums: List of integers
        target: Target sum to find
        
    Returns:
        List of two indices [i, j] where nums[i] + nums[j] == target
        Returns None if no such pair exists
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if len(nums) < 2:
        return None
        
    # Hash map to store value -> index mapping
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if complement exists in our seen values
        if complement in seen:
            # Found a pair: nums[seen[complement]] + nums[i] == target
            return [seen[complement], i]
        
        # Store current number and its index
        seen[num] = i
    
    # No pair found
    return None


# Alternative brute force implementation for comparison
def two_sum_brute_force(nums, target):
    """
    Brute force implementation for verification.
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    if len(nums) < 2:
        return None
        
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return None


if __name__ == "__main__":
    # Quick verification of the algorithm
    test_cases = [
        ([2, 7, 11, 15], 9),      # Expected: [0, 1]
        ([3, 2, 4, 6], 6),        # Expected: [0, 1] or [1, 2] 
        ([1, 2, 3], 7),           # Expected: None
        ([3, 3, 4], 6),           # Expected: [0, 1]
        ([1, 2], 3),              # Expected: [0, 1]
    ]
    
    for nums, target in test_cases:
        result = two_sum(nums, target)
        brute_result = two_sum_brute_force(nums, target)
        
        print(f"Input: {nums}, Target: {target}")
        print(f"Hash Map Result: {result}")
        print(f"Brute Force Result: {brute_result}")
        
        # Verify correctness
        if result is not None:
            assert nums[result[0]] + nums[result[1]] == target
            print(f"✓ Verification: {nums[result[0]]} + {nums[result[1]]} = {target}")
        else:
            print("✓ No solution exists")
        print()
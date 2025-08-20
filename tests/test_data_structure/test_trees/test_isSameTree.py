"""
Test cases for Same Tree problem.

Problem: Given the roots of two binary trees p and q, return true if the trees 
are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure 
and the nodes have the same values.

Test cases are designed to verify:
1. Correctness: Algorithm properly compares tree structures and values
2. Edge cases: Empty trees, single nodes, null comparisons
3. Different structures: Same values but different structure
4. Same structure: Different values but same structure
5. Complex cases: Large trees with multiple levels
"""

import unittest


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    """
    Check if two binary trees are the same.
    
    Args:
        p: TreeNode - root of first binary tree
        q: TreeNode - root of second binary tree
    
    Returns:
        bool - True if trees are equivalent, False otherwise
    
    Time Complexity: O(min(m,n)) where m,n are sizes of trees p,q
    Space Complexity: O(min(h1,h2)) where h1,h2 are heights of trees p,q
    """
    # Base case: both trees are empty
    if not p and not q:
        return True
    
    # One tree is empty, the other is not
    if not p or not q:
        return False
    
    # Both trees have nodes - compare values and recurse
    return (p.val == q.val and 
            isSameTree(p.left, q.left) and 
            isSameTree(p.right, q.right))


class TestIsSameTree(unittest.TestCase):
    
    def test_identical_trees(self):
        """
        Test Case 1: Identical trees
        Tree p:    1      Tree q:    1
                  / \                / \
                 2   3              2   3
        
        Both trees have the same structure and values.
        Expected result: True
        """
        # Create first tree
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        
        # Create second tree (identical)
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        
        self.assertTrue(isSameTree(p, q))
    
    def test_different_structure_same_values(self):
        """
        Test Case 2: Same values but different structure
        Tree p:    1      Tree q:    1
                  /                   \
                 2                     2
        
        Both trees contain the same values (1, 2) but have different structures.
        Expected result: False
        """
        # Create first tree (left child)
        p = TreeNode(1)
        p.left = TreeNode(2)
        
        # Create second tree (right child)
        q = TreeNode(1)
        q.right = TreeNode(2)
        
        self.assertFalse(isSameTree(p, q))
    
    def test_same_structure_different_values(self):
        """
        Test Case 3: Same structure but different values
        Tree p:    1      Tree q:    1
                  / \                / \
                 2   1              2   3
        
        Both trees have the same structure but different leaf values.
        Expected result: False
        """
        # Create first tree
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(1)
        
        # Create second tree (different right value)
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        
        self.assertFalse(isSameTree(p, q))
    
    def test_empty_trees(self):
        """
        Test Case 4: Both trees are empty
        Tree p: None     Tree q: None
        
        Two empty trees should be considered the same.
        Expected result: True
        """
        p = None
        q = None
        
        self.assertTrue(isSameTree(p, q))
    
    def test_one_empty_one_single_node(self):
        """
        Test Case 5: One empty tree, one with single node
        Tree p: None     Tree q:    1
        
        One tree is empty while the other has a single node.
        Expected result: False
        """
        p = None
        q = TreeNode(1)
        
        self.assertFalse(isSameTree(p, q))


if __name__ == '__main__':
    unittest.main()
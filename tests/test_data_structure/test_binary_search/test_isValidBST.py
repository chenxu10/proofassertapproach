"""
Test cases for Valid Binary Search Tree problem.

Problem: Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Test cases are designed to verify:
1. Correctness: Algorithm properly validates BST properties
2. Edge cases: Empty tree, single node, duplicate values
3. Invalid BST: Nodes violating BST property at different levels
4. Valid BST: Proper BST structure with valid ordering
5. Complex cases: Large trees with multiple levels
"""

import unittest


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):
    """
    Determine if a binary tree is a valid binary search tree.
    
    Args:
        root: TreeNode - root of the binary tree
    
    Returns:
        bool - True if tree is a valid BST, False otherwise
    
    Time Complexity: O(n) where n is the number of nodes
    Space Complexity: O(h) where h is the height of the tree
    """
    def validate(node, min_val, max_val):
        # Empty tree is valid BST
        if not node:
            return True
        
        # Check if current node violates BST property
        if node.val <= min_val or node.val >= max_val:
            return False
        
        # Recursively validate left and right subtrees with updated bounds
        return (validate(node.left, min_val = min_val, max_val = node.val) and 
                validate(node.right, min_val = node.val, max_val = max_val))
    
    return validate(root, float('-inf'), float('inf'))


class TestIsValidBST(unittest.TestCase):
    
    def test_valid_bst(self):
        """
        Test Case 1: Valid BST
        Tree:        5
                   /   \
                  3     8
                 / \   / \
                2   4 7   9
        
        All nodes satisfy BST property: left < root < right
        Expected result: True
        """
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(8)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        
        self.assertTrue(isValidBST(root))
    
    def test_invalid_bst_left_violation(self):
        """
        Test Case 2: Invalid BST - left subtree violation
        Tree:        5
                   /   \
                  3     8
                 / \   
                2   6
        
        Node 6 is in left subtree but greater than root 5.
        Expected result: False
        """
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(8)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(6)  # Violates BST property
        
        self.assertFalse(isValidBST(root))
    
    def test_invalid_bst_right_violation(self):
        """
        Test Case 3: Invalid BST - right subtree violation
        Tree:        5
                   /   \
                  3     8
                       / \
                      4   9
        
        Node 4 is in right subtree but less than root 5.
        Expected result: False
        """
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(8)
        root.right.left = TreeNode(4)  # Violates BST property
        root.right.right = TreeNode(9)
        
        self.assertFalse(isValidBST(root))
    
    def test_single_node(self):
        """
        Test Case 4: Single node tree
        Tree:    5
        
        A single node is always a valid BST.
        Expected result: True
        """
        root = TreeNode(5)
        
        self.assertTrue(isValidBST(root))
    
    def test_empty_tree(self):
        """
        Test Case 5: Empty tree
        Tree: None
        
        An empty tree is considered a valid BST.
        Expected result: True
        """
        root = None
        
        self.assertTrue(isValidBST(root))


if __name__ == '__main__':
    unittest.main()
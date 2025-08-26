"""
Test cases for Kth Smallest Element in BST problem.

Problem: Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:
- The left subtree of every node contains only nodes with keys less than the node's key.
- The right subtree of every node contains only nodes with keys greater than the node's key.  
- Both the left and right subtrees are also binary search trees.

Test cases are designed to verify:
1. Correctness: Algorithm finds the correct kth smallest element
2. Edge cases: k=1 (smallest), k=n (largest), single node
3. Different BST structures: Balanced, left-skewed, right-skewed
4. Various k values: Beginning, middle, end of sorted order
"""

import unittest
from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Find the kth smallest element in a BST using in-order traversal.
        
        Args:
            root: Optional[TreeNode] - root of the BST
            k: int - the kth position (1-indexed)
        
        Returns:
            int - the kth smallest value in the BST
        
        In-order traversal of BST visits nodes in sorted order.
        We can stop early once we find the kth element.
        """
        def inorder(node, count):
            if not node:
                return count, None
            
            # Traverse left subtree
            count, result = inorder(node.left, count)
            if result is not None:
                return count, result
            
            # Process current node
            count += 1
            if count == k:
                return count, node.val
            
            # Traverse right subtree
            return inorder(node.right, count)
        
        _, result = inorder(root, 0)
        return result

class TestKthSmallest(unittest.TestCase):
    
    def setUp(self):
        """Set up test BSTs for multiple test cases."""
        self.solution = Solution()
        
        # BST 1: Balanced BST
        #       5
        #      / \
        #     3   6
        #    / \   \
        #   2   4   8
        #  /       / \
        # 1       7   9
        # In-order: [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.root1 = TreeNode(5)
        self.root1.left = TreeNode(3)
        self.root1.right = TreeNode(6)
        self.root1.left.left = TreeNode(2)
        self.root1.left.right = TreeNode(4)
        self.root1.right.right = TreeNode(8)
        self.root1.left.left.left = TreeNode(1)
        self.root1.right.right.left = TreeNode(7)
        self.root1.right.right.right = TreeNode(9)
        
        # BST 2: Left-skewed BST
        #   5
        #  /
        # 4
        #/
        #3
        #/
        #2
        #/
        #1
        # In-order: [1, 2, 3, 4, 5]
        self.root2 = TreeNode(5)
        self.root2.left = TreeNode(4)
        self.root2.left.left = TreeNode(3)
        self.root2.left.left.left = TreeNode(2)
        self.root2.left.left.left.left = TreeNode(1)
        
        # BST 3: Right-skewed BST
        # 1
        #  \
        #   2
        #    \
        #     3
        #      \
        #       4
        #        \
        #         5
        # In-order: [1, 2, 3, 4, 5]
        self.root3 = TreeNode(1)
        self.root3.right = TreeNode(2)
        self.root3.right.right = TreeNode(3)
        self.root3.right.right.right = TreeNode(4)
        self.root3.right.right.right.right = TreeNode(5)
        
        # BST 4: Single node
        # 42
        # In-order: [42]
        self.root4 = TreeNode(42)
    
    def test_kth_smallest_balanced_tree_middle(self):
        """
        Test Case 1: Balanced BST, find middle element
        Tree: root1 (balanced BST with 9 nodes)
        In-order: [1, 2, 3, 4, 5, 6, 7, 8, 9]
        k=5 (middle element)
        Expected: 5
        
        This tests finding the kth smallest in a balanced tree
        where k is in the middle of the sorted sequence.
        """
        result = self.solution.kthSmallest(self.root1, 5)
        self.assertEqual(result, 5)
    
    def test_kth_smallest_first_element(self):
        """
        Test Case 2: Find the 1st smallest (minimum) element
        Tree: root1 (balanced BST with 9 nodes)
        In-order: [1, 2, 3, 4, 5, 6, 7, 8, 9]
        k=1 (first/smallest element)
        Expected: 1
        
        This tests finding the minimum element in the BST,
        which should be the leftmost node.
        """
        result = self.solution.kthSmallest(self.root1, 1)
        self.assertEqual(result, 1)
    
    def test_kth_smallest_last_element(self):
        """
        Test Case 3: Find the last smallest (maximum) element  
        Tree: root1 (balanced BST with 9 nodes)
        In-order: [1, 2, 3, 4, 5, 6, 7, 8, 9]
        k=9 (last/largest element)
        Expected: 9
        
        This tests finding the maximum element in the BST,
        which should be the rightmost node.
        """
        result = self.solution.kthSmallest(self.root1, 9)
        self.assertEqual(result, 9)
    
    def test_kth_smallest_left_skewed_tree(self):
        """
        Test Case 4: Left-skewed BST
        Tree: root2 (left-skewed BST)
        In-order: [1, 2, 3, 4, 5]
        k=3 (middle element)
        Expected: 3
        
        This tests the algorithm on an unbalanced tree
        that is heavily skewed to the left side.
        """
        result = self.solution.kthSmallest(self.root2, 3)
        self.assertEqual(result, 3)
    
    def test_kth_smallest_single_node(self):
        """
        Test Case 5: Single node BST
        Tree: root4 (single node with value 42)
        In-order: [42]
        k=1 (only element)
        Expected: 42
        
        This tests the edge case where the BST contains
        only one node, so the 1st smallest is that node itself.
        """
        result = self.solution.kthSmallest(self.root4, 1)
        self.assertEqual(result, 42)


if __name__ == '__main__':
    unittest.main()
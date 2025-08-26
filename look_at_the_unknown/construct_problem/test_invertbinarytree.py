"""
Test cases for Invert Binary Tree problem.

Problem: You are given the root of a binary tree root. 
Invert the binary tree and return its root.

Inverting a binary tree means swapping the left and right children 
of every node in the tree recursively.

Test cases are designed to verify:
1. Correctness: Algorithm properly inverts all nodes
2. Edge cases: Empty tree, single node, leaf nodes
3. Different structures: Balanced, unbalanced, complete trees
4. Preservation: Original tree structure is maintained (just mirrored)
"""

import unittest


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __eq__(self, other):
        """Compare TreeNode objects recursively for testing."""
        if not isinstance(other, TreeNode):
            return False
        if other is None:
            return False
        
        return (self.val == other.val and 
                self.left == other.left and 
                self.right == other.right)
    
    def to_list_level_order(self):
        """Convert tree to level-order list representation for easier testing."""
        if not self:
            return []
        
        result = []
        queue = [self]
        
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        
        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()
        
        return result


def invertTree(root):
    """
    Invert a binary tree by swapping left and right children recursively.
    
    Args:
        root: TreeNode - root of the binary tree to invert
    
    Returns:
        TreeNode - root of the inverted binary tree
    
    Heuristics: Master Theorem: T(n) = aT(log(n/b)) + f(n)
    """
    # Base case: empty tree
    if not root:
        return None
    
    # aT(log(n/b))
    right_invert = invertTree(root.right)
    left_invert = invertTree(root.left)

    # F(n)
    root.left = right_invert
    root.right = left_invert

    return root  


def invertTreeIterative(root):
    """
    Alternative solution: Invert a binary tree using iterative BFS approach.
    
    Args:
        root: TreeNode - root of the binary tree to invert
    
    Returns:
        TreeNode - root of the inverted binary tree
    
    Time Complexity: O(n) - visit each node once
    Space Complexity: O(w) where w is maximum width of tree (queue size)
    
    This approach uses a queue to traverse the tree level by level,
    swapping left and right children at each node.
    """
    if not root:
        return None
    
    # Use queue for BFS traversal
    queue = [root]
    
    while queue:
        # Process current node
        current = queue.pop(0)
        
        # Swap left and right children
        current.left, current.right = current.right, current.left
        
        # Add children to queue for processing (if they exist)
        if current.left:
            queue.append(current.left)
            
        if current.right:
            queue.append(current.right)
    
    return root

class TestInvertBinaryTree(unittest.TestCase):
    
    def test_invert_balanced_tree(self):
        """
        Test Case 1: Balanced binary tree
        Original:     4
                     / \
                    2   7
                   / \ / \
                  1  3 6  9
        
        Inverted:     4
                     / \
                    7   2
                   / \ / \
                  9  6 3  1
        
        This tests the basic functionality of inverting a complete,
        balanced binary tree with multiple levels.
        """
        # Create original tree
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)
        
        # Invert the tree
        inverted_root = invertTree(root)
        
        # Verify the structure is inverted
        self.assertEqual(inverted_root.val, 4)
        self.assertEqual(inverted_root.left.val, 7)
        self.assertEqual(inverted_root.right.val, 2)
        self.assertEqual(inverted_root.left.left.val, 9)
        self.assertEqual(inverted_root.left.right.val, 6)
        self.assertEqual(inverted_root.right.left.val, 3)
        self.assertEqual(inverted_root.right.right.val, 1)
    
    def test_invert_single_node(self):
        """
        Test Case 2: Single node tree
        Original:  1
        Inverted:  1
        
        This tests the edge case where the tree contains only
        the root node with no children.
        """
        root = TreeNode(1)
        inverted_root = invertTree(root)
        
        self.assertEqual(inverted_root.val, 1)
        self.assertIsNone(inverted_root.left)
        self.assertIsNone(inverted_root.right)
    
    def test_invert_empty_tree(self):
        """
        Test Case 3: Empty tree
        Original:  None
        Inverted:  None
        
        This tests the edge case where the input tree is empty (None).
        The function should handle this gracefully and return None.
        """
        root = None
        inverted_root = invertTree(root)
        
        self.assertIsNone(inverted_root)
    
    def test_invert_left_skewed_tree(self):
        """
        Test Case 4: Left-skewed tree (unbalanced)
        Original:    1
                    /
                   2
                  /
                 3
                /
               4
        
        Inverted:    1
                      \
                       2
                        \
                         3
                          \
                           4
        
        This tests the algorithm's behavior on an unbalanced tree
        that only has left children, ensuring it becomes right-skewed.
        """
        # Create left-skewed tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        
        # Invert the tree
        inverted_root = invertTree(root)
        
        # Verify it becomes right-skewed
        self.assertEqual(inverted_root.val, 1)
        self.assertIsNone(inverted_root.left)
        self.assertEqual(inverted_root.right.val, 2)
        self.assertIsNone(inverted_root.right.left)
        self.assertEqual(inverted_root.right.right.val, 3)
        self.assertIsNone(inverted_root.right.right.left)
        self.assertEqual(inverted_root.right.right.right.val, 4)
    
    def test_invert_asymmetric_tree(self):
        """
        Test Case 5: Asymmetric tree with mixed structure
        Original:      1
                      / \
                     2   3
                    /     \
                   4       5
                          / \
                         6   7
        
        Inverted:      1
                      / \
                     3   2
                    /     \
                   5       4
                  / \
                 7   6
        
        This tests a more complex asymmetric tree structure to ensure
        the algorithm correctly handles trees with different depths
        and structures on left and right sides.
        """
        # Create asymmetric tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.right.right = TreeNode(5)
        root.right.right.left = TreeNode(6)
        root.right.right.right = TreeNode(7)
        
        # Invert the tree
        inverted_root = invertTree(root)
        
        # Verify the inverted structure
        self.assertEqual(inverted_root.val, 1)
        self.assertEqual(inverted_root.left.val, 3)
        self.assertEqual(inverted_root.right.val, 2)
        self.assertEqual(inverted_root.left.left.val, 5)
        self.assertIsNone(inverted_root.left.right)
        self.assertIsNone(inverted_root.right.left)
        self.assertEqual(inverted_root.right.right.val, 4)
        self.assertEqual(inverted_root.left.left.left.val, 7)
        self.assertEqual(inverted_root.left.left.right.val, 6)

    def test_compare_recursive_vs_iterative(self):
        """
        Test Case 6: Compare recursive vs iterative implementations
        
        This test ensures both the recursive and iterative implementations
        produce identical results for the same input tree.
        """
        # Create test tree
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)
        root1.left.left = TreeNode(4)
        root1.left.right = TreeNode(5)
        
        # Create identical copy for second approach
        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(3)
        root2.left.left = TreeNode(4)
        root2.left.right = TreeNode(5)
        
        # Apply both approaches
        recursive_result = invertTree(root1)
        iterative_result = invertTreeIterative(root2)
        
        # Convert to lists for easy comparison
        recursive_list = recursive_result.to_list_level_order()
        iterative_list = iterative_result.to_list_level_order()
        
        # Both should produce identical results
        self.assertEqual(recursive_list, iterative_list)
        
        # Verify the actual inverted structure
        expected = [1, 3, 2, None, None, 5, 4]
        self.assertEqual(recursive_list, expected)
        self.assertEqual(iterative_list, expected)


if __name__ == '__main__':
    unittest.main() 
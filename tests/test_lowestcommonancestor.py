"""
Test cases for Lowest Common Ancestor (LCA) in Binary Search Tree.

Problem: Given a binary search tree (BST) where all node values are unique, 
and two nodes from the tree p and q, return the lowest common ancestor (LCA) 
of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a 
tree T such that both p and q are descendants. The ancestor is allowed to be 
a descendant of itself.

Test cases are designed to verify:
1. Correctness: Algorithm finds the correct LCA
2. Edge cases: Root as LCA, node as ancestor of itself
3. Different tree structures: Balanced and unbalanced trees
4. Various node positions: Left subtree, right subtree, different levels
"""

import unittest


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __eq__(self, other):
        """Compare TreeNode objects by value for testing."""
        if not isinstance(other, TreeNode):
            return False
        return self.val == other.val


def lowestCommonAncestor(root, p, q):
    """
    Find the lowest common ancestor of two nodes in a BST.
    
    Args:
        root: TreeNode - root of the BST
        p: TreeNode - first target node
        q: TreeNode - second target node
    
    Returns:
        TreeNode - the lowest common ancestor of p and q
    
    Algorithm leverages BST property:
    - If both p and q are smaller than root, LCA is in left subtree
    - If both p and q are larger than root, LCA is in right subtree
    - Otherwise, root is the LCA (one node is on each side)
    """
    # Base case: if root is None
    if not root:
        return None
    
    # If both nodes are smaller than root, LCA is in left subtree
    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    
    # If both nodes are larger than root, LCA is in right subtree
    elif p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    
    # Otherwise, root is the LCA
    # This happens when:
    # 1. One node is smaller and one is larger than root
    # 2. One of the nodes is the root itself
    else:
        return root


class TestLowestCommonAncestor(unittest.TestCase):
    
    def setUp(self):
        """Set up test trees for multiple test cases."""
        # Tree 1: Balanced BST
        #       6
        #      / \
        #     2   8
        #    / \ / \
        #   0  4 7  9
        #     / \
        #    3   5
        self.root1 = TreeNode(6)
        self.root1.left = TreeNode(2)
        self.root1.right = TreeNode(8)
        self.root1.left.left = TreeNode(0)
        self.root1.left.right = TreeNode(4)
        self.root1.right.left = TreeNode(7)
        self.root1.right.right = TreeNode(9)
        self.root1.left.right.left = TreeNode(3)
        self.root1.left.right.right = TreeNode(5)
        
        # Tree 2: Right-skewed BST
        #   2
        #    \
        #     3
        #      \
        #       4
        #        \
        #         5
        self.root2 = TreeNode(2)
        self.root2.right = TreeNode(3)
        self.root2.right.right = TreeNode(4)
        self.root2.right.right.right = TreeNode(5)
    
    def test_lca_both_in_left_subtree(self):
        """
        Test Case 1: Both nodes are in the left subtree
        Tree structure: root1 (balanced BST)
        Nodes: p=2, q=4
        Expected LCA: 2
        
        This tests the case where both target nodes are descendants
        of the left child of root, so the LCA should be found by
        recursing into the left subtree.
        """
        p = TreeNode(2)
        q = TreeNode(4)
        result = lowestCommonAncestor(self.root1, p, q)
        self.assertEqual(result.val, 2)
    
    def test_lca_both_in_right_subtree(self):
        """
        Test Case 2: Both nodes are in the right subtree
        Tree structure: root1 (balanced BST)
        Nodes: p=7, q=9
        Expected LCA: 8
        
        This tests the case where both target nodes are descendants
        of the right child of root, so the LCA should be found by
        recursing into the right subtree.
        """
        p = TreeNode(7)
        q = TreeNode(9)
        result = lowestCommonAncestor(self.root1, p, q)
        self.assertEqual(result.val, 8)
    
    def test_lca_nodes_on_different_sides(self):
        """
        Test Case 3: Nodes are on different sides of root
        Tree structure: root1 (balanced BST)
        Nodes: p=2, q=8
        Expected LCA: 6 (root)
        
        This tests the case where one node is in the left subtree
        and the other is in the right subtree, making the root
        the lowest common ancestor.
        """
        p = TreeNode(2)
        q = TreeNode(8)
        result = lowestCommonAncestor(self.root1, p, q)
        self.assertEqual(result.val, 6)
    
    def test_lca_one_node_is_ancestor(self):
        """
        Test Case 4: One node is the ancestor of the other
        Tree structure: root1 (balanced BST)
        Nodes: p=2, q=0
        Expected LCA: 2
        
        This tests the case where one of the target nodes is
        actually the ancestor of the other. The ancestor node
        itself should be returned as the LCA.
        """
        p = TreeNode(2)
        q = TreeNode(0)
        result = lowestCommonAncestor(self.root1, p, q)
        self.assertEqual(result.val, 2)
    
    def test_lca_linear_tree(self):
        """
        Test Case 5: Linear/skewed tree structure
        Tree structure: root2 (right-skewed BST)
        Nodes: p=2, q=4
        Expected LCA: 2
        
        This tests the algorithm's behavior on an unbalanced,
        linear tree structure where nodes form a chain.
        The LCA should still be found correctly.
        """
        p = TreeNode(2)
        q = TreeNode(4)
        result = lowestCommonAncestor(self.root2, p, q)
        self.assertEqual(result.val, 2)


if __name__ == '__main__':
    unittest.main() 
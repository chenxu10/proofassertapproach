"""
Test cases for Lowest Common Ancestor (LCA) in Binary Search Tree.

Problem: Given a binary search tree (BST) where all node values are unique, 
and two nodes from the tree p and q, return the lowest common ancestor (LCA) 
of the two nodes.
"""

import unittest
from typing import Optional, Tuple
from unittest import TestCase


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right
    
    def __eq__(self, other) -> bool:
        """Compare TreeNode objects by value for testing."""
        if not isinstance(other, TreeNode):
            return False
        return self.val == other.val
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"TreeNode({self.val})"


def lowestCommonAncestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
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
    if not root:
        return None
    
    if p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    elif p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    else:
        # Invariant: LCA value must be between min(p.val, q.val) and max(p.val, q.val)
        assert min(p.val, q.val) <= root.val <= max(p.val, q.val), f"LCA invariant violated: {root.val} not between {min(p.val, q.val)} and {max(p.val, q.val)}"
        return root
    
class TestLowestCommonAncestor(unittest.TestCase):
    
    def setUp(self):
        """Set up test trees for multiple test cases."""
        self.balanced_tree = self._create_balanced_bst()
        self.skewed_tree = self._create_right_skewed_bst()
        self.single_node_tree = TreeNode(42)
    
    def _create_balanced_bst(self) -> TreeNode:
        """Create a balanced BST for testing.
        
        Tree structure:
               6
              / \
             2   8
            / \ / \
           0  4 7  9
             / \
            3   5
        """
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        return root
    
    def _create_right_skewed_bst(self) -> TreeNode:
        """Create a right-skewed BST for testing.
        
        Tree structure:
           2
            \
             3
              \
               4
                \
                 5
        """
        root = TreeNode(2)
        root.right = TreeNode(3)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(5)
        return root
    
    def _find_node_by_value(self, root: TreeNode, val: int) -> Optional[TreeNode]:
        """Helper method to find a node by its value in the tree."""
        if not root:
            return None
        if root.val == val:
            return root
        if val < root.val:
            return self._find_node_by_value(root.left, val)
        else:
            return self._find_node_by_value(root.right, val)
    
    def test_lca_both_in_left_subtree(self):
        """
        Test Case 1: Both nodes are in the left subtree
        Tree structure: balanced BST
        Nodes: p=2, q=4
        Expected LCA: 2
        
        This tests the case where both target nodes are descendants
        of the left child of root, so the LCA should be found by
        recursing into the left subtree.
        """
        p = self._find_node_by_value(self.balanced_tree, 2)
        q = self._find_node_by_value(self.balanced_tree, 4)
        result = lowestCommonAncestor(self.balanced_tree, p, q)
        self.assertEqual(result.val, 2)
    
    def test_lca_both_in_right_subtree(self):
        """
        Test Case 2: Both nodes are in the right subtree
        Tree structure: balanced BST
        Nodes: p=7, q=9
        Expected LCA: 8
        
        This tests the case where both target nodes are descendants
        of the right child of root, so the LCA should be found by
        recursing into the right subtree.
        """
        p = self._find_node_by_value(self.balanced_tree, 7)
        q = self._find_node_by_value(self.balanced_tree, 9)
        result = lowestCommonAncestor(self.balanced_tree, p, q)
        self.assertEqual(result.val, 8)
    
    def test_lca_nodes_on_different_sides(self):
        """
        Test Case 3: Nodes are on different sides of root
        Tree structure: balanced BST
        Nodes: p=2, q=8
        Expected LCA: 6 (root)
        
        This tests the case where one node is in the left subtree
        and the other is in the right subtree, making the root
        the lowest common ancestor.
        """
        p = self._find_node_by_value(self.balanced_tree, 2)
        q = self._find_node_by_value(self.balanced_tree, 8)
        result = lowestCommonAncestor(self.balanced_tree, p, q)
        self.assertEqual(result.val, 6)
    
    def test_lca_one_node_is_ancestor(self):
        """
        Test Case 4: One node is the ancestor of the other
        Tree structure: balanced BST
        Nodes: p=2, q=0
        Expected LCA: 2
        
        This tests the case where one of the target nodes is
        actually the ancestor of the other. The ancestor node
        itself should be returned as the LCA.
        """
        p = self._find_node_by_value(self.balanced_tree, 2)
        q = self._find_node_by_value(self.balanced_tree, 0)
        result = lowestCommonAncestor(self.balanced_tree, p, q)
        self.assertEqual(result.val, 2)
    
    def test_lca_linear_tree(self):
        """
        Test Case 5: Linear/skewed tree structure
        Tree structure: right-skewed BST
        Nodes: p=2, q=4
        Expected LCA: 2
        
        This tests the algorithm's behavior on an unbalanced,
        linear tree structure where nodes form a chain.
        The LCA should still be found correctly.
        """
        p = self._find_node_by_value(self.skewed_tree, 2)
        q = self._find_node_by_value(self.skewed_tree, 4)
        result = lowestCommonAncestor(self.skewed_tree, p, q)
        self.assertEqual(result.val, 2)
    
    def test_lca_root_is_target_node(self):
        """
        Test Case 6: Root is one of the target nodes
        Tree structure: balanced BST
        Nodes: p=6 (root), q=3
        Expected LCA: 6
        
        This tests the case where the root itself is one of the target nodes.
        """
        p = self._find_node_by_value(self.balanced_tree, 6)
        q = self._find_node_by_value(self.balanced_tree, 3)
        result = lowestCommonAncestor(self.balanced_tree, p, q)
        self.assertEqual(result.val, 6)
    
    def test_lca_single_node_tree(self):
        """
        Test Case 7: Single node tree
        Tree structure: single node (42)
        Nodes: p=42, q=42
        Expected LCA: 42
        
        This tests the edge case of a tree with only one node.
        """
        p = self.single_node_tree
        q = self.single_node_tree
        result = lowestCommonAncestor(self.single_node_tree, p, q)
        self.assertEqual(result.val, 42)
    
    def test_lca_none_root(self):
        """
        Test Case 8: Empty tree (None root)
        Tree structure: None
        Nodes: p=TreeNode(1), q=TreeNode(2)
        Expected LCA: None
        
        This tests the edge case of an empty tree.
        """
        p = TreeNode(1)
        q = TreeNode(2)
        result = lowestCommonAncestor(None, p, q)
        self.assertIsNone(result)
    
    def test_lca_leaf_nodes_same_parent(self):
        """
        Test Case 9: Leaf nodes with same parent
        Tree structure: balanced BST
        Nodes: p=3, q=5 (both children of node 4)
        Expected LCA: 4
        
        This tests finding LCA of two leaf nodes that share the same parent.
        """
        p = self._find_node_by_value(self.balanced_tree, 3)
        q = self._find_node_by_value(self.balanced_tree, 5)
        result = lowestCommonAncestor(self.balanced_tree, p, q)
        self.assertEqual(result.val, 4)
    
    def test_lca_parametrized_cases(self):
        """
        Parametrized test cases for comprehensive LCA testing.
        
        Each test case is a tuple of (tree_type, p_val, q_val, expected_lca_val, description).
        This approach reduces code duplication and makes it easy to add new test cases.
        """
        test_cases = [
            ('balanced', 2, 4, 2, 'Both in left subtree'),
            ('balanced', 7, 9, 8, 'Both in right subtree'), 
            ('balanced', 2, 8, 6, 'Different sides of root'),
            ('balanced', 2, 0, 2, 'One is ancestor of other'),
            ('balanced', 6, 3, 6, 'Root is target node'),
            ('balanced', 3, 5, 4, 'Leaf nodes same parent'),
            ('skewed', 2, 4, 2, 'Linear tree structure'),
            ('skewed', 3, 5, 3, 'Sequential nodes in skewed tree'),
        ]
        
        for tree_type, p_val, q_val, expected_lca, description in test_cases:
            with self.subTest(tree=tree_type, p=p_val, q=q_val, desc=description):
                tree = self.balanced_tree if tree_type == 'balanced' else self.skewed_tree
                p = self._find_node_by_value(tree, p_val)
                q = self._find_node_by_value(tree, q_val)
                
                self.assertIsNotNone(p, f"Node {p_val} not found in {tree_type} tree")
                self.assertIsNotNone(q, f"Node {q_val} not found in {tree_type} tree")
                
                result = lowestCommonAncestor(tree, p, q)
                self.assertEqual(result.val, expected_lca, 
                               f"Failed for {description}: expected {expected_lca}, got {result.val}")


if __name__ == '__main__':
    unittest.main() 
"""
Test cases for Binary Tree Serialization and Deserialization problem.

Problem: Implement an algorithm to serialize and deserialize a binary tree.
Serialization is the process of converting an in-memory structure into a sequence 
of bits so that it can be stored or sent across a network to be reconstructed later.

Test cases are designed to verify:
1. Round-trip correctness: serialize then deserialize returns original tree
2. Empty tree handling
3. Single node tree
4. Complex tree structures
5. Edge cases with unbalanced trees
"""

import unittest
from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    """
    Codec for binary tree serialization and deserialization.
    Uses preorder traversal with null markers for serialization.
    """
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Encodes a tree to a single string using preorder traversal.
        
        Args:
            root: Optional[TreeNode] - root of the binary tree
            
        Returns:
            str - serialized representation of the tree
            
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(n) for the result string
        """
        vals = []
        
        def dfs(node):
            if not node:
                vals.append("null")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(vals)
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        Decodes encoded data to recreate the binary tree.
        
        Args:
            data: str - serialized tree representation
            
        Returns:
            Optional[TreeNode] - root of the reconstructed tree
            
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(n) for recursion stack and node creation
        """
        vals = data.split(",")
        self.i = 0
        
        def dfs():
            if vals[self.i] == "null":
                self.i += 1
                return None
            
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()


def trees_equal(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    """
    Helper function to compare two binary trees for structural and value equality.
    """
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return (root1.val == root2.val and 
            trees_equal(root1.left, root2.left) and 
            trees_equal(root1.right, root2.right))


class TestSerializeDeserialize(unittest.TestCase):
    
    def setUp(self):
        self.codec = Codec()
    
    def test_empty_tree(self):
        """
        Test Case 1: Empty tree
        Tree: None
        
        Should handle null root correctly.
        Expected: serialize returns "null", deserialize returns None
        """
        root = None
        serialized = self.codec.serialize(root)
        deserialized = self.codec.deserialize(serialized)
        
        self.assertTrue(trees_equal(root, deserialized))
        self.assertEqual(serialized, "null")
    
    def test_single_node(self):
        """
        Test Case 2: Single node tree
        Tree:    5
        
        Simple case with only root node.
        Expected: Round-trip should preserve single node
        """
        root = TreeNode(5)
        serialized = self.codec.serialize(root)
        deserialized = self.codec.deserialize(serialized)
        
        self.assertTrue(trees_equal(root, deserialized))
    
    def test_complete_binary_tree(self):
        """
        Test Case 3: Complete binary tree
        Tree:        1
                   /   \
                  2     3
                 / \   / \
                4   5 6   7
        
        Balanced tree with all levels filled.
        Expected: Perfect round-trip preservation
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        serialized = self.codec.serialize(root)
        deserialized = self.codec.deserialize(serialized)
        
        self.assertTrue(trees_equal(root, deserialized))
    
    def test_unbalanced_tree(self):
        """
        Test Case 4: Unbalanced tree (left-skewed)
        Tree:    1
               /
              2
             /
            3
           /
          4
        
        Tests handling of highly unbalanced structures.
        Expected: Maintains tree structure after round-trip
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        
        serialized = self.codec.serialize(root)
        deserialized = self.codec.deserialize(serialized)
        
        self.assertTrue(trees_equal(root, deserialized))
    
    def test_mixed_structure_with_nulls(self):
        """
        Test Case 5: Mixed structure with null children
        Tree:        1
                   /   \
                  2     3
                   \   /
                    4 5
        
        Tests proper handling of trees with selective null children.
        Expected: Exact structure preservation including null positions
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(5)
        
        serialized = self.codec.serialize(root)
        deserialized = self.codec.deserialize(serialized)
        
        self.assertTrue(trees_equal(root, deserialized))


if __name__ == '__main__':
    unittest.main()
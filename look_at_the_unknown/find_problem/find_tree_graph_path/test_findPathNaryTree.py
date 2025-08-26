import unittest
from typing import List, Optional


class TreeNode:
    """N-ary tree node definition"""
    def __init__(self, val: int = 0, children: List['TreeNode'] = None):
        self.val = val
        self.children = children if children is not None else []


def find_path_in_nary_tree(root: Optional[TreeNode], target: int) -> List[int]:
    """
    Find the path from root to target node in an N-ary tree.
    
    Problem Description:
    Given an N-ary tree and a target value, find the path from root to the node
    containing the target value. Return the path as a list of node values.
    If target is not found, return an empty list.
    
    ASCII Diagram Example:
           1
         / | \
        2  3  4
       /|     |\
      5 6     7 8
                |
                9
    
    find_path_in_nary_tree(root, 9) -> [1, 4, 8, 9]
    find_path_in_nary_tree(root, 6) -> [1, 2, 6]
    find_path_in_nary_tree(root, 10) -> []
    
    Data Flow:
    1. Start from root, add current node to path
    2. If current node equals target, return path
    3. For each child, recursively search
    4. If found in child subtree, return path
    5. If not found in any child, backtrack (remove current node)
    6. Return empty list if target not found
    
    Args:
        root: Root of the N-ary tree
        target: Target value to find
        
    Returns:
        List of node values representing path from root to target,
        empty list if target not found
        
    Time Complexity: O(n) where n is number of nodes
    Space Complexity: O(h) where h is height of tree (recursion stack)
    """
    # TODO: Implement the solution
    pass

    # base case
    if not root or target is None:
        return []

    # init a path
    path = []

    # dfs(root, target)
    def dfs(root, target, path):
        path.append(root.val)
        if root.val == target:
            return True

        for child in root.children:
            if dfs(child, target, path):
                return True

        path.pop()
        return False

    # return path
    if dfs(root, target, path):
        return path
    else:
        return []


class TestFindPathNaryTree(unittest.TestCase):
    
    def setUp(self):
        """Set up test trees"""
        # Tree 1: Simple 3-level tree
        #     1
        #   / | \
        #  2  3  4
        # /|     |\
        #5 6     7 8
        #          |
        #          9
        self.tree1 = TreeNode(1)
        self.tree1.children = [
            TreeNode(2, [TreeNode(5), TreeNode(6)]),
            TreeNode(3),
            TreeNode(4, [TreeNode(7), TreeNode(8, [TreeNode(9)])])
        ]
        
        # Tree 2: Single node
        self.tree2 = TreeNode(42)
        
        # Tree 3: Linear tree (like a linked list)
        #  1
        #  |
        #  2
        #  |
        #  3
        self.tree3 = TreeNode(1, [TreeNode(2, [TreeNode(3)])])
        
    def test_target_exists_leaf_node(self):
        """Test finding path to a leaf node"""
        result = find_path_in_nary_tree(self.tree1, 9)
        expected = [1, 4, 8, 9]
        self.assertEqual(result, expected)
        
    def test_target_exists_internal_node(self):
        """Test finding path to an internal node"""
        result = find_path_in_nary_tree(self.tree1, 4)
        expected = [1, 4]
        self.assertEqual(result, expected)
        
    def test_target_is_root(self):
        """Test when target is the root node"""
        result = find_path_in_nary_tree(self.tree1, 1)
        expected = [1]
        self.assertEqual(result, expected)
        
    def test_target_not_found(self):
        """Test when target doesn't exist in tree"""
        result = find_path_in_nary_tree(self.tree1, 99)
        expected = []
        self.assertEqual(result, expected)
        
    def test_single_node_tree(self):
        """Test with single node tree"""
        result = find_path_in_nary_tree(self.tree2, 42)
        expected = [42]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
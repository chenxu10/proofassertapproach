import pytest
from typing import Optional, List
from collections import deque


def levelOrder(node):
    """
    Binary Tree Level Order Traversal (BFS)
    
    Data Flow Diagram:
    ==================
    
    Example Tree (from test_complete_binary_tree):
           3
          / \
         9  20
           /  \
          15   7
    
    Step-by-Step Queue Processing:
    
    Initial:
    Queue: [3]          Result: []
           ↑
         front
    
    Level 0:
    Queue: [9, 20]      Result: [[3]]
           ↑     ↑
         front  back
         (process 3 → add children 9,20)
    
    Level 1:  
    Queue: [15, 7]      Result: [[3], [9, 20]]
           ↑    ↑
         front back
         (process 9,20 → add children 15,7)
    
    Level 2:
    Queue: []           Result: [[3], [9, 20], [15, 7]]
                        (process 15,7 → no children)
    
    Algorithm Flow:
    ┌─────────────┐    ┌──────────────────┐    ┌─────────────────┐
    │ dequeue()   │ →  │ collect values   │ →  │ enqueue()       │
    │ cur_node    │    │ into cur_level   │    │ left & right    │
    └─────────────┘    └──────────────────┘    └─────────────────┘
           ↑                    ↓                        ↓
           └──── while queue ←──┴── append to result ←───┘
    
    Time: O(n), Space: O(w) where w is max width of tree
    """
    def enqueue_children(queue, node):
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    if not node:
        return []
    
    result = []
    queue = deque([node])

    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.val)
            enqueue_children(queue, current_node)

        result.append(current_level)

    return result


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestLevelOrder:
    def test_empty_tree(self):
        """Test level order traversal of an empty tree"""
        result = levelOrder(None)
        assert result == []

    def test_single_node(self):
        """Test level order traversal of a single node tree"""
        root = TreeNode(1)
        result = levelOrder(root)
        assert result == [[1]]

    def test_complete_binary_tree(self):
        """Test level order traversal of a complete binary tree"""
        # Tree:     3
        #          / \
        #         9  20
        #           /  \
        #          15   7
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        
        result = levelOrder(root)
        assert result == [[3], [9, 20], [15, 7]]

    def test_left_skewed_tree(self):
        """Test level order traversal of a left-skewed tree"""
        # Tree: 1
        #      /
        #     2
        #    /
        #   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        
        result = levelOrder(root)
        assert result == [[1], [2], [3]]

    def test_mixed_structure_tree(self):
        """Test level order traversal of a tree with mixed structure"""
        # Tree:       1
        #           /   \
        #          2     3
        #         /     / \
        #        4     5   6
        #       /
        #      7
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(6)
        root.left.left.left = TreeNode(7)
        
        result = levelOrder(root)
        assert result == [[1], [2, 3], [4, 5, 6], [7]]


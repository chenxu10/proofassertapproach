"""
Test cases for Subtree of Another Tree problem.

Problem: Given the roots of two binary trees root and subRoot, return true if there 
is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree is a tree that consists of a node in the original tree 
and all of its descendants. The tree could also be considered as a subtree of itself.

Test cases are designed to verify:
1. Correctness: Algorithm properly identifies valid subtrees
2. Edge cases: Empty trees, single nodes, identical trees
3. Structure matching: Same structure and values at different positions
4. False positives: Similar but not identical subtrees
5. Complex cases: Large trees with nested potential subtrees
"""

import unittest


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root, subRoot):
    """
    Check if subRoot is a subtree of root.
    
    Args:
        root: TreeNode - root of the main binary tree
        subRoot: TreeNode - root of the potential subtree
    
    Returns:
        bool - True if subRoot is a subtree of root, False otherwise
    
    Algorithm Mental Model (Data Flow Diagram):
    ==========================================
    
    Main Tree:        3              SubRoot:     4
                     / \                         / \
                    4   5                       1   2
                   / \
                  1   2
    
    Step-by-Step Data Flow:
    ┌─────────────────────────────────────────────────────────────────┐
    │ 1. isSubtree(root=3, subRoot=[4,1,2])                          │
    │    ├─ Base Cases: root≠None, subRoot≠None → Continue           │
    │    ├─ isSameTree(3, 4) → False (values don't match)           │
    │    └─ Recurse: isSubtree(left=4) OR isSubtree(right=5)        │
    │                                                                │
    │ 2. isSubtree(root=4, subRoot=[4,1,2])                          │
    │    ├─ isSameTree(4, 4) → Check structure match                │
    │    │  ├─ Values match: 4 == 4 ✓                              │
    │    │  ├─ Left subtrees: isSameTree(1, 1) ✓                   │
    │    │  └─ Right subtrees: isSameTree(2, 2) ✓                  │
    │    └─ Returns: True → FOUND MATCH!                            │
    └─────────────────────────────────────────────────────────────────┘
    
    Traversal Pattern (Preorder):
    ┌───┬───┬───┬───┬───┐
    │ 3 │ 4 │ 1 │ 2 │ 5 │  ← Check each node as potential subtree root
    └───┴───┴───┴───┴───┘
      ↓   ↓   ↓   ↓   ↓
      ✗   ✓   ✗   ✗   ✗    ← Only node 4 produces exact match
    
    Two-Phase Algorithm:
    Phase 1: Traverse main tree to find candidate nodes
    Phase 2: For each candidate, perform deep structural comparison
    
    ┌─ Traversal Strategy ─┐    ┌─ Comparison Strategy ─┐
    │ • Visit each node    │    │ • Compare values      │
    │ • Check if potential │ → │ • Recurse left       │
    │ • Continue if no     │    │ • Recurse right      │
    │   match found        │    │ • All must match     │
    └─────────────────────┘    └──────────────────────┘
    
    Hints:
    - Think about two main operations: finding potential matching nodes and comparing subtrees
    - Consider using a helper function to check if two trees are identical
    - Base cases: What happens when root is None? When subRoot is None?
    - Recursive approach: Check current node, then check left and right subtrees
    - Time Complexity: O(m * n) where m is nodes in root, n is nodes in subRoot
    """
    # TODO: Implement the subtree checking algorithm
    # Hint 1: Handle base cases first (None inputs)
    if root is None and subRoot is not None:
        return False
    
    if subRoot is None:
        return True
    # Hint 2: Use a helper function isSameTree to check if two trees are identical
    if isSameTree(root, subRoot):
        return True
    
    # Hint 3: For each node in root, check if subtree starting there matches subRoot
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)
    

def isSameTree(p, q):
    """
    Helper function to check if two trees are identical.
    
    Args:
        p: TreeNode - root of first tree
        q: TreeNode - root of second tree
    
    Returns:
        bool - True if trees are identical, False otherwise
    
    Hints:
    - This is similar to the same tree problem
    - Base cases: both None (True), one None (False)
    - Recursive cases: compare values and recurse on children
    """
    # TODO: Implement tree comparison
    # Hint: Check values match and recursively compare left/right subtrees
    if p is None and q is None:
        return True
    if p is None and q is not None:
        return False
    if q is None and p is not None:
        return False
    if p.val != q.val:
        return False
    leftsame = isSameTree(p.left,q.left)
    rightsame = isSameTree(p.right, q.right)
    return leftsame and rightsame


class TestIsSubtree(unittest.TestCase):
    
    def test_valid_subtree_at_left(self):
        """
        Test Case 1: Valid subtree found at left child
        Main tree:       3        Subtree:    4
                        / \                  / \
                       4   5                1   2
                      / \
                     1   2
        
        The subtree [4,1,2] appears as the left subtree of the main tree.
        Expected result: True
        
        Hints for implementation:
        - Start checking from root (3), doesn't match subRoot (4)
        - Move to left child (4), check if this subtree matches subRoot
        - Use isSameTree helper to compare the subtrees starting at node 4
        """
        # Create main tree
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        
        # Create subtree
        subRoot = TreeNode(4)
        subRoot.left = TreeNode(1)
        subRoot.right = TreeNode(2)
        
        self.assertTrue(isSubtree(root, subRoot))
    
    def test_invalid_subtree_extra_node(self):
        """
        Test Case 2: Similar structure but subtree has extra node
        Main tree:       3        Subtree:    4
                        / \                  / \
                       4   5                1   2
                      / \                      /
                     1   2                    0
        
        The potential subtree at node 4 doesn't match because subRoot has 
        an extra node (0) that doesn't exist in the main tree.
        Expected result: False
        
        Hints for implementation:
        - When comparing at node 4, the structures don't match exactly
        - The right child (2) in main tree has no left child
        - The right child (2) in subRoot has a left child (0)
        - This should return False during the isSameTree comparison
        """
        # Create main tree
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        
        # Create subtree with extra node
        subRoot = TreeNode(4)
        subRoot.left = TreeNode(1)
        subRoot.right = TreeNode(2)
        subRoot.right.left = TreeNode(0)
        
        self.assertFalse(isSubtree(root, subRoot))
    
    def test_identical_trees(self):
        """
        Test Case 3: Entire tree is the subtree
        Main tree:    1        Subtree:    1
                     / \                   / \
                    2   3                 2   3
        
        When the main tree and subtree are identical, the result should be True.
        This tests the case where the subtree is the entire tree.
        Expected result: True
        
        Hints for implementation:
        - The first comparison at root should immediately return True
        - This tests that your algorithm handles the "tree as subtree of itself" case
        """
        # Create main tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        
        # Create identical subtree
        subRoot = TreeNode(1)
        subRoot.left = TreeNode(2)
        subRoot.right = TreeNode(3)
        
        self.assertTrue(isSubtree(root, subRoot))
    
    def test_subtree_not_found(self):
        """
        Test Case 4: Subtree pattern doesn't exist in main tree
        Main tree:       3        Subtree:    6
                        / \                  / \
                       4   5                7   8
                      / \
                     1   2
        
        The subtree pattern [6,7,8] doesn't appear anywhere in the main tree.
        Expected result: False
        
        Hints for implementation:
        - Algorithm should traverse all nodes in main tree
        - None of the nodes (3,4,5,1,2) match the subRoot value (6)
        - Should return False after checking all possibilities
        - Make sure to handle the recursive calls correctly
        """
        # Create main tree
        root = TreeNode(3)
        root.left = TreeNode(4)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        
        # Create non-matching subtree
        subRoot = TreeNode(6)
        subRoot.left = TreeNode(7)
        subRoot.right = TreeNode(8)
        
        self.assertFalse(isSubtree(root, subRoot))
    
    def test_empty_subtree(self):
        """
        Test Case 5: Empty subtree (None)
        Main tree:    1        Subtree: None
                     / \
                    2   3
        
        An empty subtree (None) should be considered a subtree of any tree.
        This tests the edge case handling for null inputs.
        Expected result: True
        
        Hints for implementation:
        - This is a base case in your algorithm
        - When subRoot is None, what should the function return?
        - Consider: is an empty tree a subtree of any tree?
        - This tests your base case handling at the start of the function
        """
        # Create main tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        
        # Empty subtree
        subRoot = None
        
        self.assertTrue(isSubtree(root, subRoot))

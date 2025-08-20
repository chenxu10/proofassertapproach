"""
Test cases for Binary Tree Maximum Path Sum problem based on constructive proof approach.

The Binary Tree Maximum Path Sum problem: Given a binary tree, find the maximum 
path sum. The path may start and end at any node in the tree.

Test cases are designed to verify proof requirements:
1. Correctness: Solution finds the actual maximum path sum
2. Completeness: Handles all tree structures (linear, balanced, single node, etc.)
3. Termination: Algorithm terminates for all finite binary trees
4. Edge cases: Negative values, single nodes, empty trees
5. Path validity: Ensures paths are valid (connected nodes)

Mathematical Induction Proof: Postorder Traversal Visits All Nodes

Theorem: Postorder traversal visits every node in a binary tree exactly once.

Definition: Postorder traversal visits nodes in the order: Left → Right → Root
Algorithm:
    postorder(node):
        if node is not None:
            postorder(node.left)   # Visit left subtree
            postorder(node.right)  # Visit right subtree
            visit(node)            # Visit current node

Proof by Structural Induction:

Base Cases:
1. Empty Tree (node = None):
   - Algorithm terminates immediately without visiting any nodes
   - Vacuously true: visits all 0 nodes exactly once ✓

2. Single Node Tree (leaf node):
   - node.left = None, node.right = None
   - No recursive calls made
   - visit(node) called exactly once
   - Visits the single node exactly once ✓

Inductive Hypothesis:
Assume postorder traversal correctly visits all nodes exactly once for:
- Any left subtree L with |L| nodes
- Any right subtree R with |R| nodes
where |L|, |R| < n (smaller than current tree size)

Inductive Step:
Consider a tree T with root node and subtrees L, R where |T| = |L| + |R| + 1 = n

Execution trace:
1. postorder(root.left):
   - By inductive hypothesis: visits all |L| nodes in left subtree exactly once
   - Let this set be S_L = {v₁, v₂, ..., v|L|}

2. postorder(root.right):
   - By inductive hypothesis: visits all |R| nodes in right subtree exactly once
   - Let this set be S_R = {u₁, u₂, ..., u|R|}

3. visit(root):
   - Visits root node exactly once
   - Root ∉ S_L ∪ S_R (by tree structure property)

Total nodes visited: S_L ∪ S_R ∪ {root}

Completeness Proof:
- |S_L ∪ S_R ∪ {root}| = |L| + |R| + 1 = n (all nodes in T)
- S_L, S_R, {root} are pairwise disjoint (tree property)
- Therefore, all n nodes in tree T are visited

Uniqueness Proof (each node visited exactly once):
- Each node v ∈ S_L visited exactly once (by inductive hypothesis)
- Each node u ∈ S_R visited exactly once (by inductive hypothesis)  
- Root visited exactly once (single visit() call)
- No node appears in multiple sets (tree structure ensures disjoint subtrees)
- Therefore, each node visited exactly once

Termination Proof:
- Each recursive call operates on a proper subtree (smaller size)
- Base case (None) terminates immediately
- Tree has finite size, so recursion depth is finite
- Algorithm must terminate

Conclusion:
By mathematical induction, postorder traversal visits every node in any finite binary tree exactly once.

This proof establishes the correctness foundation for algorithms that rely on postorder traversal,
such as the maxPathSum algorithm below.
"""

import unittest


def maxPathSum(node):
    """
    Binary Tree Maximum Path Sum - Find the maximum sum of any path in a binary tree.
    
    ASCII Diagram of Key Concepts:
    
    Example Tree:        1
                       /   \
                      2     3
                     / \   
                    4   5   
    
    Two types of paths to consider at each node:
    1. Path THROUGH current node (connects left & right subtrees):
       Path: 4 → 2 → 5  (sum = 11, goes THROUGH node 2)
       
    2. Path FROM current node (extends upward to parent):
       Path: 4 → 2 → 1  (node 2 contributes: 2 + max(left=4, right=5) = 7)
    
    Key Insight: At each node, we need to:
    - Update global maximum with path THROUGH this node
    - Return path FROM this node to parent
    
    Think About:
    1. Why do we use postorder traversal? (Hint: what do we need before processing current node?)
    2. What's the difference between "path through node" vs "path from node"?
    3. Why return only one direction (left OR right) to parent?
    """
    # TODO 1: Initialize global maximum. What should be the initial value?
    # Hint: Consider what happens with all-negative trees
    global_max_sum = float('-inf')  # Safe initial value for all cases including all-negative trees

    def post_order_traversal(node):
        """
        Returns: Maximum path sum FROM this node going upward (to parent)
        Side effect: Updates global_max_sum with path THROUGH this node
        
        Think: Why do we need both return value AND side effect?
        """
        nonlocal global_max_sum
        
        # TODO 2: Base case - what to return for empty node?
        # Hint: What value doesn't affect parent's sum calculation?
        if not node:
            return 0  # Return 0 so it doesn't contribute to parent's calculation
            
        # TODO 3: Get maximum contributions from children
        # Hint: Postorder means process children first. Why?
        left_contribution = post_order_traversal(node.left)  # Get raw contribution from left
        right_contribution = post_order_traversal(node.right)  # Get raw contribution from right
        
        # Only take positive contributions (ignore negative paths)
        left_max = max(0, left_contribution)
        right_max = max(0, right_contribution)
        
        # TODO 4: Calculate path THROUGH current node (left → node → right)
        # This is a candidate for global maximum but can't extend to parent
        # Why? Because it uses BOTH left and right paths
        current_max = node.val + left_max + right_max
        
        # TODO 5: Update global maximum
        # Compare current path through this node with global best
        global_max_sum = max(current_max, global_max_sum)
            
        # TODO 6: Return path FROM this node (extending upward)
        # Key insight: Can only choose ONE direction (left OR right) + current node
        # Why? Because parent can only connect through current node in one direction
        return node.val + max(left_max, right_max)  # Return max path from this node upward
        
        # Reflection Questions:
        # - Why can't we return current_max to parent?
        # - What would happen if we always chose both left_max + right_max?
        # - How does this handle negative contributions?

    post_order_traversal(node)
    return global_max_sum

class TreeNode:
    """Binary tree node definition for testing"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestBinaryMaxPathSum(unittest.TestCase):
    
    def test_simple_positive_tree(self):
        """
        Test Case 1: Simple tree with all positive values
        Proof requirement: Correctness - finds maximum path in basic case
        
        Tree:     2
                 / \
                1   3
                
        Expected: 6 (path: 1 -> 2 -> 3)
        
        This verifies the algorithm correctly identifies the maximum path
        when all values are positive and path goes through root.
        """
        # Construct tree: 1-2-3
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        
        # Expected maximum path sum is 1 + 2 + 3 = 6
        # Test will verify max_path_sum(root) returns 6
        actual = maxPathSum(root)
        assert actual == 6
    
    def test_negative_values_tree(self):
        """
        Test Case 2: Tree with negative values
        Proof requirement: Handles negative values correctly
        
        Tree:    -10
                 / \
                9   20
                   / \
                  15  7
                  
        Expected: 42 (path: 15 -> 20 -> 7, avoiding negative root)
        
        This tests that the algorithm correctly avoids negative nodes
        when they don't contribute to the maximum path.
        """
        # Construct tree with negative root
        root = TreeNode(-10)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        
        # Expected: 15 + 20 + 7 = 42 (avoiding the negative root -10)
        actual = maxPathSum(root)
        self.assertEqual(actual, 42)
    
    def test_single_node_tree(self):
        """
        Test Case 3: Single node tree
        Proof requirement: Termination and correctness for base cases
        
        Tree: 5
        Expected: 5 (the node itself is the maximum path)
        
        This tests the algorithm's behavior on the smallest possible
        valid input, ensuring proper base case handling.
        """
        root = TreeNode(5)
        
        # Expected: 5 (single node path)
        # This verifies correct handling of base case
        actual = maxPathSum(root)
        self.assertEqual(actual, 5)
    
    def test_linear_tree_structure(self):
        """
        Test Case 4: Linear tree (essentially a linked list)
        Proof requirement: Handles degenerate tree structures
        
        Tree:    1
                  \
                   2
                    \
                     3
                     
        Expected: 6 (path: 1 -> 2 -> 3)
        
        This tests that the algorithm works correctly on trees that
        degenerate into linear structures, proving structural completeness.
        """
        # Construct linear tree: 1->2->3
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        
        # Expected: 1 + 2 + 3 = 6
        actual = maxPathSum(root)
        self.assertEqual(actual, 6)
    
    def test_path_not_through_root(self):
        """
        Test Case 5: Maximum path doesn't include root
        Proof requirement: Considers all possible paths
        
        Tree:     1
                 / \
                2   3
               / \
              4   5
              
        Expected: 11 (path: 4 -> 2 -> 5, not including root)
        
        This verifies the algorithm considers paths that don't necessarily
        go through the root node, demonstrating algorithmic completeness.
        """
        # Construct tree where max path is in subtree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        
        # Expected: 4 + 2 + 5 = 11 (left subtree path)
        actual = maxPathSum(root)
        self.assertEqual(actual, 11)
    
    def test_all_negative_values(self):
        """
        Test Case 6: Tree with all negative values
        Proof requirement: Handles worst-case scenarios correctly
        
        Tree:    -3
                 / \
               -4  -5
               
        Expected: -3 (single node with least negative value)
        
        This tests the algorithm's behavior when all values are negative,
        ensuring it returns the least negative single node.
        """
        # Construct all-negative tree
        root = TreeNode(-3)
        root.left = TreeNode(-4)
        root.right = TreeNode(-5)
        
        # Expected: -3 (best single node when all are negative)
        actual = maxPathSum(root)
        self.assertEqual(actual, -3)
    
    def test_mixed_large_tree(self):
        """
        Test Case 7: Larger mixed positive/negative tree
        Proof requirement: Scales correctly with tree size
        
        Tree:      5
                  / \
                 4   8
                /   / \
               11  13  4
              / \      \
             7   2      1
             
        Expected: 48 (path: 7 -> 11 -> 4 -> 5 -> 8 -> 13)
        
        This tests algorithmic correctness on larger trees with
        mixed positive and negative values.
        """
        # Construct larger mixed tree
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)
        
        # Expected: 48 (path: 7 -> 11 -> 4 -> 5 -> 8 -> 13)
        actual = maxPathSum(root)
        self.assertEqual(actual, 48)


if __name__ == '__main__':
    unittest.main()
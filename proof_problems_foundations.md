# Foundational Proof Problems in Data Structures and Algorithms

## Problem 1: Array Access Time Complexity
**Problem Statement:** Prove that accessing an element at a specific index in an array takes O(1) time complexity.

**Requirements:**
- Define what O(1) means in terms of constant time
- Explain the mathematical relationship between array indexing and memory addresses
- Show that the number of operations does not depend on array size
- Demonstrate that `array[i]` requires the same number of steps regardless of i or array length

## Problem 2: Linear Search Correctness
**Problem Statement:** Prove that linear search algorithm correctly finds an element if it exists in an array, or correctly reports that it doesn't exist.

### Algorithm Definition

```python
def linear_search(arr, target):
    """
    Linear search algorithm with proof assertions
    
    Precondition: arr is a list, target is the element to find
    Postcondition: returns index if found, -1 if not found
    """
    n = len(arr)
    
    # Loop invariant: target is not in arr[0:i]
    for i in range(n):
        # Invariant holds: target ∉ arr[0:i] before each iteration
        assert all(arr[j] != target for j in range(i)), "Invariant violated: target found before index i"
        
        if arr[i] == target:
            # Found target at index i
            assert arr[i] == target, "Correctness: found element matches target"
            return i
    
    # Loop completed: target ∉ arr[0:n], so target not in array
    assert all(arr[j] != target for j in range(n)), "Completeness: target not in entire array"
    return -1
```

### Formal Proof

**1. Algorithm Definition:**
- Input: Array `arr` of length `n`, target element `target`
- Output: Index `i` where `arr[i] == target`, or `-1` if no such index exists

**2. Loop Invariant:**
At the start of each iteration `i`, the target element is not present in `arr[0:i]`.
- **Mathematical form:** ∀j ∈ [0, i), arr[j] ≠ target

**3. Proof of Correctness:**

**Base Case (i = 0):**
- Before first iteration: `arr[0:0]` is empty
- Invariant trivially holds: target ∉ ∅

**Inductive Step:**
- **Assume:** Invariant holds at iteration `i` (target ∉ arr[0:i])
- **Case 1:** `arr[i] == target`
  - Algorithm returns `i` 
  - **Correctness:** `arr[i] == target` ✓
- **Case 2:** `arr[i] ≠ target`  
  - Continue to `i+1`
  - **Invariant maintenance:** target ∉ arr[0:i] ∧ arr[i] ≠ target → target ∉ arr[0:i+1] ✓

**4. Termination:**
- Loop executes at most `n` iterations
- Variable `i` increases by 1 each iteration: 0 → 1 → ... → n-1
- **Termination guaranteed:** `i < n` becomes false after finite steps

**5. Completeness:**
**Case A - Element Found:**
- If ∃k ∈ [0, n) such that arr[k] == target
- Algorithm reaches iteration `k` (by termination proof)
- At iteration `k`: arr[k] == target, so algorithm returns `k` ✓

**Case B - Element Not Found:**  
- If ∀j ∈ [0, n), arr[j] ≠ target
- Loop completes all `n` iterations without returning
- Final invariant: target ∉ arr[0:n] = target not in entire array
- Algorithm returns `-1` ✓

### Proof Summary
- **Correctness:** If target exists, algorithm finds it (Case A)
- **Completeness:** If target doesn't exist, algorithm reports -1 (Case B)  
- **Termination:** Algorithm halts in ≤ n steps
- **Loop Invariant:** Maintains target ∉ arr[0:i] throughout execution

## Problem 3: Binary Search Time Complexity
**Problem Statement:** Prove that binary search on a sorted array of n elements has time complexity O(log n).

**Requirements:**
- Define the binary search algorithm precisely
- Show that each iteration reduces the search space by half
- Prove that the maximum number of iterations is ⌈log₂(n)⌉
- Demonstrate why this leads to O(log n) complexity
- Include base case and recursive analysis

## Problem 4: Stack LIFO Property
**Problem Statement:** Prove that a properly implemented stack data structure maintains the Last-In-First-Out (LIFO) property.

**Requirements:**
- Define the stack operations: push, pop, and top
- Prove that the last element pushed is always the first to be popped
- Show that the order of popping is the reverse of the order of pushing
- Use mathematical induction on the sequence of operations
- Handle edge cases (empty stack, single element)

## Problem 5: Queue FIFO Property
**Problem Statement:** Prove that a properly implemented queue data structure maintains the First-In-First-Out (FIFO) property.

**Requirements:**
- Define the queue operations: enqueue and dequeue
- Prove that elements are removed in the same order they were added
- Show that the first element enqueued is the first to be dequeued
- Use sequence notation to formalize the ordering
- Address the relationship between enqueue and dequeue operations

## Problem 6: Bubble Sort Correctness
**Problem Statement:** Prove that the bubble sort algorithm correctly sorts an array in ascending order.

**Requirements:**
- Define the bubble sort algorithm with precise steps
- Prove using loop invariants that after k passes, the last k elements are in their correct positions
- Show that the algorithm terminates after at most n-1 passes
- Prove that upon termination, the entire array is sorted
- Handle cases where the array is already sorted or has duplicate elements

## Problem 7: Insertion Sort Time Complexity
**Problem Statement:** Prove that insertion sort has worst-case time complexity O(n²) and best-case time complexity O(n).

**Requirements:**
- Define the insertion sort algorithm precisely
- Identify the worst-case scenario (reverse-sorted array)
- Count the number of comparisons and shifts in the worst case
- Identify the best-case scenario (already sorted array)
- Show mathematical derivation of both time complexities
- Explain why average case is also O(n²)

## Problem 8: Linked List Insertion Complexity
**Problem Statement:** Prove that inserting an element at the beginning of a singly linked list takes O(1) time, while inserting at a specific position takes O(n) time in the worst case.

**Requirements:**
- Define the structure of a singly linked list
- Show that insertion at the head requires constant number of operations
- Prove that insertion at position k requires traversing k nodes
- Demonstrate that worst-case insertion (at the end) requires O(n) traversal
- Compare with array insertion complexities

## Problem 9: Binary Tree Height and Node Relationship
**Problem Statement:** Prove that a binary tree with n nodes has height at least ⌈log₂(n+1)⌉ - 1 and at most n - 1.

**Requirements:**
- Define binary tree, height, and node count precisely
- Prove the minimum height bound (complete binary tree case)
- Prove the maximum height bound (degenerate tree case)
- Show that these bounds are tight by providing examples
- Use mathematical induction or direct counting arguments

## Problem 10: Hash Table Average Case Complexity
**Problem Statement:** Prove that under uniform hashing assumption, the average time complexity for search, insert, and delete operations in a hash table is O(1 + α), where α is the load factor.

**Requirements:**
- Define uniform hashing assumption and load factor α = n/m
- Prove the expected number of elements in each bucket is α
- Show that successful search takes expected time O(1 + α/2)
- Show that unsuccessful search takes expected time O(1 + α)
- Explain why this leads to O(1) average case when α is constant
- Address the relationship between load factor and performance

## Problem 11: Binary Tree Traversal Completeness
**Problem Statement:** Prove that depth-first search (DFS) traversals (preorder, inorder, postorder) visit every node in a binary tree exactly once.

**Requirements:**
- Define preorder, inorder, and postorder traversal algorithms
- Prove by structural induction that each traversal visits all nodes
- Show that no node is visited more than once in any traversal
- Demonstrate the recursive structure of the proof
- Address base cases (empty tree, single node, left/right subtrees)

## Problem 12: Graph DFS Correctness
**Problem Statement:** Prove that depth-first search on a graph visits every vertex reachable from the starting vertex exactly once.

**Requirements:**
- Define DFS algorithm with visited array/set
- Prove that all reachable vertices are eventually visited
- Show that no vertex is visited more than once
- Use strong induction on the structure of recursive calls
- Handle both recursive and iterative implementations
- Address disconnected components

## Problem 13: BFS Shortest Path Property
**Problem Statement:** Prove that breadth-first search finds the shortest path (minimum number of edges) from source to any reachable vertex in an unweighted graph.

**Requirements:**
- Define BFS algorithm with queue-based implementation
- Prove that vertices are discovered in order of increasing distance
- Show that when a vertex is first discovered, the path to it is shortest
- Use induction on the BFS tree levels
- Demonstrate why the queue maintains the correct ordering
- Handle the case where multiple shortest paths exist

## Problem 14: Graph Cycle Detection using DFS
**Problem Statement:** Prove that DFS can correctly detect cycles in both directed and undirected graphs using appropriate edge classification.

**Requirements:**
- Define DFS edge types: tree, back, forward, cross edges
- For directed graphs: prove that a back edge indicates a cycle
- For undirected graphs: prove that a back edge (not to parent) indicates a cycle
- Show that absence of back edges means the graph is acyclic
- Use DFS timestamps and vertex states (white, gray, black)
- Address the correctness of cycle detection algorithm

## Problem 15: Dynamic Programming Optimal Substructure
**Problem Statement:** Prove that the Fibonacci sequence computation using dynamic programming has optimal substructure and overlapping subproblems properties.

**Requirements:**
- Define optimal substructure: optimal solution contains optimal solutions to subproblems
- Show that F(n) = F(n-1) + F(n-2) exhibits optimal substructure
- Prove the overlapping subproblems property by showing repeated computations
- Compare naive recursive vs. DP approaches in terms of time complexity
- Demonstrate that memoization eliminates redundant computations
- Show time complexity reduction from O(2^n) to O(n)

## Problem 16: Longest Common Subsequence DP Correctness
**Problem Statement:** Prove that the dynamic programming solution for Longest Common Subsequence (LCS) correctly computes the length of the LCS for any two strings.

**Requirements:**
- Define LCS problem and recurrence relation precisely
- Prove that the DP recurrence correctly handles all cases:
  - Characters match: LCS(i,j) = 1 + LCS(i-1,j-1)
  - Characters don't match: LCS(i,j) = max(LCS(i-1,j), LCS(i,j-1))
- Show that the base cases are correct (empty strings)
- Prove by induction that DP[i][j] gives the correct LCS length
- Demonstrate optimal substructure property

## Problem 17: Tree Height Calculation via Recursion
**Problem Statement:** Prove that the recursive algorithm for calculating tree height correctly computes the height for any binary tree.

**Requirements:**
- Define tree height as the longest path from root to leaf
- Define the recursive height algorithm: height(node) = 1 + max(height(left), height(right))
- Prove correctness using strong induction on tree structure
- Handle base cases: empty tree (height -1 or 0), single node (height 0 or 1)
- Show that the algorithm correctly handles all tree shapes
- Address the relationship between recursive calls and tree structure

## Problem 18: Graph Connectivity via DFS
**Problem Statement:** Prove that running DFS from every unvisited vertex correctly identifies all connected components in an undirected graph.

**Requirements:**
- Define connected components in an undirected graph
- Describe the algorithm: for each unvisited vertex, run DFS to mark all reachable vertices
- Prove that vertices in the same DFS tree belong to the same connected component
- Show that vertices in different DFS trees belong to different connected components
- Demonstrate that the algorithm finds all connected components
- Use graph theory definitions and properties of connectivity

## Problem 19: Binary Search Tree Property Preservation
**Problem Statement:** Prove that insertion and deletion operations in a Binary Search Tree preserve the BST property.

**Requirements:**
- Define BST property: for any node, left subtree values < node value < right subtree values
- For insertion: prove that inserting a value maintains BST property
- For deletion: prove that all three deletion cases preserve BST property:
  - Node with no children
  - Node with one child  
  - Node with two children (successor replacement)
- Show that the inorder traversal remains sorted after operations
- Use structural induction on the tree

## Problem 20: Dynamic Programming Space Optimization
**Problem Statement:** Prove that space-optimized dynamic programming solutions (using O(min(m,n)) space instead of O(m×n)) produce the same results as the standard 2D table approach.

**Requirements:**
- Choose a specific DP problem (e.g., LCS, Edit Distance, or Knapsack)
- Show that only the previous row/column is needed for current computations
- Prove that rolling arrays or 1D arrays preserve correctness
- Demonstrate that the recurrence relation dependencies are satisfied
- Show that the final result is identical to the 2D approach
- Address the trade-offs between space and time complexity

---

## General Proof Guidelines

For each problem, your proof should include:
1. **Clear definitions** of all terms and data structures used
2. **Precise algorithm descriptions** where applicable
3. **Mathematical rigor** with proper notation and logic
4. **Base cases and inductive steps** where appropriate
5. **Consideration of edge cases** and boundary conditions
6. **Clear reasoning** for each step of the proof
7. **Proper complexity analysis** using Big-O notation where relevant
import pytest
from typing import Optional

class ListNode:
    """Doubly Linked List Node for LRU Cache"""
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev: Optional['ListNode'] = None
        self.next: Optional['ListNode'] = None

class LRUCache:
    """
    LRU (Least Recently Used) Cache Implementation
    
    COMPLEXITY ANALYSIS (Master Theorem Application):
    Time: O(1) for both get() and put() operations
    Space: O(capacity) for storing key-value pairs
    
    ALGORITHM PATTERN: Hash Table + Doubly Linked List
    - Hash table: O(1) access to any node
    - Doubly linked list: O(1) insertion/deletion at ends
    - Combined: O(1) for all operations
    
    This does NOT fit Master Theorem form T(n) = aT(n/b) + f(n)
    because it's data structure operations, not divide-and-conquer.
    
    LRU CACHE VISUALIZATION:
    ========================
    
    INITIAL STATE (Empty Cache, Capacity = 3):
    
    Hash Table (cache):     Doubly Linked List:
    ┌──────────────────┐    ┌──────┐    ┌──────┐
    │     cache: {}    │    │ HEAD │◄──►│ TAIL │
    │                  │    │(dummy)    │(dummy)│
    └──────────────────┘    └──────┘    └──────┘
    
    AFTER put(1, 100):
    
    Hash Table:             Doubly Linked List:
    ┌──────────────────┐    ┌──────┐    ┌─────────┐    ┌──────┐
    │ cache: {         │    │ HEAD │◄──►│ k:1,v:100│◄──►│ TAIL │
    │   1 → Node(1,100)│    │(dummy)    │  (MRU)   │    │(dummy)│
    │ }                │    └──────┘    └─────────┘    └──────┘
    └──────────────────┘         ▲            ▲            ▲
                                 │            │            │
                         Hash table points to this node
    
    AFTER put(2, 200):
    
    Hash Table:             Doubly Linked List:
    ┌──────────────────┐    ┌──────┐    ┌─────────┐    ┌─────────┐    ┌──────┐
    │ cache: {         │    │ HEAD │◄──►│ k:2,v:200│◄──►│ k:1,v:100│◄──►│ TAIL │
    │   1 → Node(1,100)│    │(dummy)    │  (MRU)   │    │  (LRU)   │    │(dummy)│
    │   2 → Node(2,200)│    └──────┘    └─────────┘    └─────────┘    └──────┘
    │ }                │         ▲            ▲            ▲            ▲
    └──────────────────┘         │     Hash points here   │            │
                                 │                        │            │
                         Most Recently Used        Least Recently Used
    
    AFTER get(1):  // Moves key 1 to head (most recently used)
    
    Hash Table:             Doubly Linked List:
    ┌──────────────────┐    ┌──────┐    ┌─────────┐    ┌─────────┐    ┌──────┐
    │ cache: {         │    │ HEAD │◄──►│ k:1,v:100│◄──►│ k:2,v:200│◄──►│ TAIL │
    │   1 → Node(1,100)│    │(dummy)    │  (MRU)   │    │  (LRU)   │    │(dummy)│
    │   2 → Node(2,200)│    └──────┘    └─────────┘    └─────────┘    └──────┘
    │ }                │
    └──────────────────┘    Usage order changed: 1 is now MRU, 2 is now LRU
    
    AFTER put(3, 300) with capacity=2:  // Evicts LRU (key 2)
    
    Hash Table:             Doubly Linked List:
    ┌──────────────────┐    ┌──────┐    ┌─────────┐    ┌─────────┐    ┌──────┐
    │ cache: {         │    │ HEAD │◄──►│ k:3,v:300│◄──►│ k:1,v:100│◄──►│ TAIL │
    │   1 → Node(1,100)│    │(dummy)    │  (MRU)   │    │  (LRU)   │    │(dummy)│
    │   3 → Node(3,300)│    └──────┘    └─────────┘    └─────────┘    └──────┘
    │ }                │
    └──────────────────┘    Key 2 was evicted (removed from both hash table and list)
    
    KEY INSIGHTS:
    - Hash table provides O(1) access to any node
    - Doubly linked list maintains usage order (MRU at head, LRU at tail)
    - Dummy head/tail simplify insertion/deletion (no null checks)
    - Both structures stay synchronized during all operations
    
    COGNITIVE LOAD ANALYSIS (Following Laws of Nature):
    - Constructor parameters: 1 (follows 7±2 rule)
    - Method parameters: ≤2 per method (within cognitive limits)
    - Single responsibility per method
    - Clear separation of concerns
    
    ALGORITHM INVARIANTS:
    1. Cache size never exceeds capacity
    2. Most recently used item is at head
    3. Least recently used item is at tail
    4. Hash table and linked list stay synchronized
    5. All operations maintain O(1) time complexity
    
    IMPLEMENTATION GUIDANCE (Following Laws of Nature):
    
    1. INITIALIZATION (Law of Error Proneness):
       # Set up capacity, hash table, and dummy head/tail nodes
       # TODO: Initialize capacity, cache dict, and dummy nodes
       # TODO: Connect dummy head and tail nodes
    
    2. HELPER METHODS (Law of Chunking):
       # Break complex operations into smaller, focused methods
       # TODO: Implement _add_to_head(node) - add node after dummy head
       # TODO: Implement _remove_node(node) - remove node from list
       # TODO: Implement _move_to_head(node) - move existing node to head
       # TODO: Implement _remove_tail() - remove node before dummy tail
    
    3. GET OPERATION (Law of Sequential Processing):
       # Follow consistent order: check -> update position -> return
       # TODO: Check if key exists in cache
       # TODO: If exists: move to head (mark as recently used) and return value
       # TODO: If not exists: return -1
    
    4. PUT OPERATION (Law of Limited Working Memory):
       # Handle two cases: update existing vs add new
       # TODO: If key exists: update value and move to head
       # TODO: If key doesn't exist:
       #   - Create new node
       #   - Add to head and cache
       #   - If over capacity: remove LRU (tail) from both list and cache
    
    COMMON ERRORS TO AVOID (Law of Error Proneness):
    - Forgetting to update both hash table AND linked list
    - Not handling capacity overflow correctly
    - Breaking linked list connections during node operations
    - Off-by-one errors in capacity management
    - Memory leaks from not properly removing nodes
    """

    def __init__(self, capacity: int):
        """
        Initialize LRU Cache with given capacity
        
        STORAGE STRENGTHENING EXERCISE:
        Think about what data structures you need:
        - What stores the key-value mappings for O(1) access?
        - What maintains the usage order for O(1) updates?
        - How do you connect head and tail initially?
        
        TODO: Implement initialization
        """
        if capacity <= 0:
            return ValueError("Capacity must larger than 0")
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
 

    def _add_to_head(self, node: ListNode) -> None:
        """
        Add node right after dummy head (most recently used position)
        
        STORAGE STRENGTHENING EXERCISE:
        Visualize the doubly linked list operations:
        
        BEFORE:
        ┌──────┐    ┌─────────┐    ┌─────────┐    ┌──────┐
        │ HEAD │◄──►│ old_first│◄──►│   ...   │◄──►│ TAIL │
        │(dummy)    │          │    │         │    │(dummy)│
        └──────┘    └─────────┘    └─────────┘    └──────┘
        
        NEW NODE TO INSERT:
        ┌─────────┐
        │new_node │
        │         │
        └─────────┘
        
        AFTER:
        ┌──────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌──────┐
        │ HEAD │◄──►│new_node │◄──►│ old_first│◄──►│   ...   │◄──►│ TAIL │
        │(dummy)    │  (MRU)  │    │          │    │         │    │(dummy)│
        └──────┘    └─────────┘    └─────────┘    └─────────┘    └──────┘
        
        STEPS NEEDED:
        1. new_node.prev = head
        2. new_node.next = head.next  
        3. head.next.prev = new_node
        4. head.next = new_node
        
        What connections need to be updated?
        TODO: Implement adding node after head
        """
        # TODO: Set new node's connections
        # TODO: Update existing nodes' connections
        # TODO: Maintain doubly-linked structure
        pass

    def _remove_node(self, node: ListNode) -> None:
        """
        Remove node from doubly linked list
        
        STORAGE STRENGTHENING EXERCISE:
        Think about pointer manipulation:
        
        BEFORE:
        ┌─────────┐    ┌─────────┐    ┌─────────┐
        │prev_node│◄──►│target   │◄──►│next_node│
        │         │    │ (remove)│    │         │
        └─────────┘    └─────────┘    └─────────┘
        
        AFTER:
        ┌─────────┐                   ┌─────────┐
        │prev_node│◄─────────────────►│next_node│
        │         │                   │         │
        └─────────┘                   └─────────┘
        
        ┌─────────┐
        │target   │ ← Isolated (ready for garbage collection)
        │ (removed)│
        └─────────┘
        
        STEPS NEEDED:
        1. node.prev.next = node.next
        2. node.next.prev = node.prev
        
        TODO: Implement node removal
        """
        # TODO: Connect previous node to next node
        # TODO: Connect next node to previous node
        pass

    def _move_to_head(self, node: ListNode) -> None:
        """
        Move existing node to head (mark as recently used)
        
        STORAGE STRENGTHENING EXERCISE:
        This combines two operations - can you identify them?
        
        BEFORE (node is somewhere in middle):
        ┌──────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌──────┐
        │ HEAD │◄──►│  node3  │◄──►│  target │◄──►│  node1  │◄──►│ TAIL │
        │(dummy)    │         │    │ (move)  │    │         │    │(dummy)│
        └──────┘    └─────────┘    └─────────┘    └─────────┘    └──────┘
        
        STEP 1: Remove from current position
        ┌──────┐    ┌─────────┐                   ┌─────────┐    ┌──────┐
        │ HEAD │◄──►│  node3  │◄─────────────────►│  node1  │◄──►│ TAIL │
        │(dummy)    │         │                   │         │    │(dummy)│
        └──────┘    └─────────┘                   └─────────┘    └──────┘
        
        ┌─────────┐
        │  target │ ← Temporarily isolated
        │ (move)  │
        └─────────┘
        
        STEP 2: Add to head position  
        ┌──────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌──────┐
        │ HEAD │◄──►│  target │◄──►│  node3  │◄──►│  node1  │◄──►│ TAIL │
        │(dummy)    │  (MRU)  │    │         │    │         │    │(dummy)│
        └──────┘    └─────────┘    └─────────┘    └─────────┘    └──────┘
        
        TODO: Use existing helper methods
        """
        # TODO: Remove node from current position
        # TODO: Add node to head position
        pass

    def _remove_tail(self) -> ListNode:
        """
        Remove and return the node before dummy tail (LRU item)
        
        STORAGE STRENGTHENING EXERCISE:
        Which node should be removed in LRU policy?
        TODO: Implement LRU removal
        """
        # TODO: Identify the LRU node
        # TODO: Remove it from list
        # TODO: Return the removed node
        pass

    def get(self, key: int) -> int:
        """
        Get value by key, mark as recently used
        
        STORAGE STRENGTHENING EXERCISE:
        What happens when you access an item in LRU cache?
        - Where should it move in the usage order?
        - What if the key doesn't exist?
        
        TODO: Implement get operation
        """
        # TODO: Check if key exists in cache
        # TODO: If exists: move to head and return value  
        # TODO: If not exists: return -1
        pass

    def put(self, key: int, value: int) -> None:
        """
        Put key-value pair, handle capacity overflow
        
        STORAGE STRENGTHENING EXERCISE:
        Consider two scenarios:
        1. Key already exists - what do you update?
        2. Key is new - what happens if cache is full?
        
        TODO: Implement put operation
        """
        # TODO: Check if key already exists
        # TODO: If exists: update value and move to head
        # TODO: If new key:
        #   - Create new node
        #   - Add to head and cache
        #   - If over capacity: remove LRU item
        pass


class TestLRUCache:
    """
    Test Suite for LRU Cache - Focus on Storage Strengthening
    
    Following Laws of Nature Principles:
    - Law of Limited Working Memory: 6 test categories (within 7±2)
    - Law of Chunking: Tests grouped by functionality
    - Law of Sequential Processing: Tests progress from simple to complex
    - Law of Pattern Recognition: Consistent test structure
    """

    # CATEGORY 1: INITIALIZATION TESTS
    def test_cache_initialization(self):
        """Test cache creation with different capacities"""
        # STORAGE STRENGTHENING: Think about edge cases for capacity
        # What should happen with capacity 1? capacity 0? negative capacity?
        # TODO: Create caches with different capacities
        # TODO: Add assertions to verify proper initialization
        lru_cache = LRUCache(1)
        assert lru_cache.capacity == 1

        with pytest.raises(ValueError):
            LRUCache(-1)

    def test_empty_cache_get(self):
        """Test getting from empty cache"""
        lru_cache = LRUCache(1)
        lru_cache.put(2)
        assert lru_cache.get(1) == -1
        assert lru_cache.get(0) == -1

    # CATEGORY 2: BASIC OPERATIONS
    def test_single_put_get(self):
        """Test basic put and get operations"""
        # STORAGE STRENGTHENING: Trace through the linked list changes
        # After put(1, 100), what's the list structure?
        # After get(1), does anything change?
        # TODO: Put one item and get it back
        # TODO: Add assertions for value and cache state
        pass

    def test_multiple_put_get(self):
        """Test multiple puts and gets without eviction"""
        # STORAGE STRENGTHENING: Track the usage order
        # After put(1,1), put(2,2), get(1), what's the LRU order?
        # TODO: Add multiple items within capacity
        # TODO: Access items in different orders
        # TODO: Add assertions for all operations
        pass

    def test_update_existing_key(self):
        """Test updating value for existing key"""
        # STORAGE STRENGTHENING: What changes besides the value?
        # Does updating a key affect its position in LRU order?
        # TODO: Put key-value, then update with new value
        # TODO: Add assertions for value update and position change
        pass

    # CATEGORY 3: CAPACITY MANAGEMENT
    def test_capacity_one_eviction(self):
        """Test LRU eviction with capacity 1"""
        # STORAGE STRENGTHENING: Simplest eviction scenario
        # With capacity 1: put(1,1), put(2,2) - what happens to key 1?
        # TODO: Create cache with capacity 1
        # TODO: Add two items and test eviction
        # TODO: Add assertions for what's evicted and what remains
        pass

    def test_capacity_overflow_basic(self):
        """Test LRU eviction with larger capacity"""
        # STORAGE STRENGTHENING: Track which item gets evicted
        # With capacity 2: put(1,1), put(2,2), put(3,3) - which is evicted?
        # TODO: Fill cache to capacity, then add one more
        # TODO: Add assertions for evicted item and remaining items
        pass

    def test_access_pattern_eviction(self):
        """Test eviction based on access patterns"""
        # STORAGE STRENGTHENING: Usage order affects eviction
        # put(1,1), put(2,2), get(1), put(3,3) - now which is LRU?
        # TODO: Create access pattern that changes LRU order
        # TODO: Add new item to trigger eviction
        # TODO: Add assertions for which item was evicted
        pass

    # CATEGORY 4: EDGE CASES
    def test_repeated_access_same_key(self):
        """Test repeatedly accessing the same key"""
        # STORAGE STRENGTHENING: Redundant operations
        # Does get(1), get(1), get(1) change anything?
        # TODO: Access same key multiple times
        # TODO: Add assertions for cache state stability
        pass

    def test_put_zero_and_negative_values(self):
        """Test edge cases with special values"""
        # STORAGE STRENGTHENING: Boundary value testing
        # How does cache handle 0, -1, or other special values?
        # TODO: Test with zero values, negative values
        # TODO: Add assertions for proper storage and retrieval
        pass

    def test_alternating_put_get_pattern(self):
        """Test complex interleaved operations"""
        # STORAGE STRENGTHENING: Complex operation sequences
        # put(1,1), get(2), put(2,2), get(1), put(3,3), get(2) - trace this!
        # TODO: Create complex sequence of puts and gets
        # TODO: Add assertions at each step to verify correctness
        pass

    # CATEGORY 5: STRESS TESTS
    def test_large_capacity_operations(self):
        """Test cache with larger capacity"""
        # STORAGE STRENGTHENING: Scale testing
        # How does cache behave with capacity 100 and many operations?
        # TODO: Create large cache and perform many operations
        # TODO: Add assertions for correctness at scale
        pass

    def test_full_cycle_eviction(self):
        """Test complete eviction cycle"""
        # STORAGE STRENGTHENING: Full replacement scenario
        # Fill cache, then replace every item - trace the evictions
        # TODO: Fill cache completely, then replace all items
        # TODO: Add assertions for each eviction step
        pass

    # CATEGORY 6: INTEGRATION TESTS
    def test_leetcode_example_1(self):
        """Test with LeetCode example 1"""
        # STORAGE STRENGTHENING: Real-world test case
        # ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        # [[2], [1,1], [2,2], [1], [3,3], [2], [4,4], [1], [3], [4]]
        # Expected: [null, null, null, 1, null, -1, null, -1, 3, 4]
        # TODO: Implement the exact sequence from LeetCode
        # TODO: Add assertions for each expected result
        pass

    def test_leetcode_example_2(self):
        """Test with LeetCode example 2"""
        # STORAGE STRENGTHENING: Another real-world scenario
        # Create your own complex test case based on LeetCode patterns
        # TODO: Design a comprehensive test sequence
        # TODO: Add detailed assertions for expected behavior
        pass


if __name__ == "__main__":
    test_suite = TestLRUCache()
    
    print("LRU Cache Test Suite")
    print("Storage Strengthening Focus - Laws of Nature Design")
    print("=" * 65)
    
    # Test categories for storage strengthening (following 7±2 cognitive limit)
    test_categories = [
        ("Initialization Tests", [
            "test_cache_initialization",
            "test_empty_cache_get"
        ]),
        ("Basic Operations", [
            "test_single_put_get", 
            "test_multiple_put_get",
            "test_update_existing_key"
        ]),
        ("Capacity Management", [
            "test_capacity_one_eviction",
            "test_capacity_overflow_basic", 
            "test_access_pattern_eviction"
        ]),
        ("Edge Cases", [
            "test_repeated_access_same_key",
            "test_put_zero_and_negative_values",
            "test_alternating_put_get_pattern"
        ]),
        ("Stress Tests", [
            "test_large_capacity_operations",
            "test_full_cycle_eviction"
        ]),
        ("Integration Tests", [
            "test_leetcode_example_1",
            "test_leetcode_example_2"
        ])
    ]
    
    total_passed = 0
    total_tests = 0
    
    for category_name, test_list in test_categories:
        print(f"\n{category_name}:")
        print("-" * 50)
        
        for test_name in test_list:
            try:
                test_method = getattr(test_suite, test_name)
                test_method()
                print(f"  ✓ {test_name}")
                total_passed += 1
            except Exception as e:
                print(f"  ✗ {test_name}: {e}")
            except NotImplementedError:
                print(f"  - {test_name}: TODO (not implemented)")
            total_tests += 1
    
    print("\n" + "=" * 65)
    print(f"Test Results: {total_passed}/{total_tests} passed")
    print("\nStorage Strengthening Principles Applied:")
    print("• Students generate their own test cases and assertions")
    print("• Focus on understanding LRU behavior through testing")
    print("• Progressive complexity from basic to integration tests")
    print("• Emphasis on tracing data structure state changes")
    print("• Real-world examples for practical application")
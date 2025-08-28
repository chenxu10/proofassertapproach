import pytest

class SnapArray:
    """
    Snap Array Data Structure Implementation
    
    COMPLEXITY ANALYSIS:
    - put(index, val): O(1) amortized
    - get(index, snap_id): O(log S) where S is number of snapshots for that index
    - snap(): O(1)
    
    ALGORITHM PATTERN: Linear Updates List + Sequential Search
    - Single list storing all updates as (snap_count, index, value) tuples
    - Each update tagged with unique snap_count identifier
    - Sequential search through updates for lookups
    
    SNAP ARRAY VISUALIZATION:
    =========================
    
    INITIAL STATE (Length = 3):
    
    snap_count: 0
    updates: []
    
    AFTER put(0, 5):
    
    snap_count: 0
    updates: [(0, 0, 5)]
             snap_count, index, value
    
    AFTER snap() -> returns snap_id = 0:
    
    snap_count: 1 (incremented)
    updates: [(0, 0, 5)]
    
    AFTER put(0, 6):
    
    snap_count: 1
    updates: [(0, 0, 5), (1, 0, 6)]
    
    AFTER put(1, 10), put(1, 11):
    
    snap_count: 1
    updates: [(0, 0, 5), (1, 0, 6), (1, 1, 10), (1, 1, 11)]
    
    AFTER snap() -> returns snap_id = 1:
    
    snap_count: 2 (incremented)
    updates: [(0, 0, 5), (1, 0, 6), (1, 1, 10), (1, 1, 11)]
    
    GET OPERATION EXAMPLES:
    - get(0, 0) -> 5 (find latest update for index 0 with snap_count <= 0)
    - get(0, 1) -> 6 (find latest update for index 0 with snap_count <= 1)
    - get(1, 1) -> 11 (find latest update for index 1 with snap_count <= 1)
    - get(1, 0) -> 0 (no updates for index 1 with snap_count <= 0)
    
    KEY INSIGHTS:
    - All updates stored in single chronological list
    - Each update tagged with unique snap_count identifier
    - Sequential search finds most recent value for given constraints
    - Default value is 0 if no matching updates found
    
    IMPLEMENTATION GUIDANCE:
    
    1. INITIALIZATION:
       # TODO: Initialize length, current snap_count, and updates list
       # TODO: Updates list starts empty
    
    2. PUT OPERATION:
       # TODO: Append (snap_count, index, value) tuple to updates list
       # TODO: Use current snap_count as unique identifier
    
    3. GET OPERATION:
       # TODO: Search through updates list for matching index and snap_count <= target
       # TODO: Return most recent matching value, or 0 if none found
    
    4. SNAP OPERATION:
       # TODO: Increment snap_count and return previous value
    """
    
    def __init__(self, length: int):
        """
        Initialize SnapArray with given length
        
        STORAGE STRENGTHENING EXERCISE:
        Think about what data structures you need:
        - How do you track the current snapshot count?
        - How do you store values with their unique snap identifiers?
        - What's the initial state of each index?
        
        TODO: Implement initialization
        """
        if length <= 0:
            raise ValueError("Length must be greater than 0")
        
        self.length = length
        self.snap_count = 0
        # Store all updates as list of (snap_count, index, value) tuples
        self.updates = []
    
    def put(self, index: int, val: int) -> None:
        """
        Set value at index in current snapshot
        
        STORAGE STRENGTHENING EXERCISE:
        Consider what needs to be updated:
        - Where do you store the new value?
        - Which snap_count should it be associated with?
        - What if the same index is updated multiple times in same snapshot?
        
        TODO: Implement put operation
        """
        if not (0 <= index < self.length):
            raise IndexError(f"Index {index} out of bounds for length {self.length}")
        
        # Store the update with current snap_count as unique identifier
        self.updates.append((self.snap_count, index, val))
    
    def snap(self) -> int:
        """
        Create a snapshot and return its ID
        
        STORAGE STRENGTHENING EXERCISE:
        What needs to happen when creating a snapshot?
        - What ID should be returned?
        - How do you prepare for the next snapshot?
        
        TODO: Implement snap operation
        """
        current_snap = self.snap_count
        self.snap_count += 1
        return current_snap
    
    def get(self, index: int, snap_id: int) -> int:
        """
        Get value at index for given snapshot ID
        
        STORAGE STRENGTHENING EXERCISE:
        Think about the lookup process:
        - How do you search through updates list using snap_count?
        - How do you find the most recent value before or at snap_id?
        - What's the default value if no updates occurred?
        
        ASCII DIAGRAM for get(index=0, snap_id=5):
        
        Updates: [(1,0,10), (3,0,20), (7,0,30)]
        
        Timeline: 0---1---2---3---4---5---6---7---8---
        Values:   0  10  10  20  20  20  20  30  30
                          ^           ^
                    snap_count=3  target=5
        
        Answer: 20 (most recent value with snap_count <= snap_id=5)
        
        TODO: Implement get operation searching through updates list
        """
        if not (0 <= index < self.length):
            raise IndexError(f"Index {index} out of bounds for length {self.length}")
        
        if snap_id < 0:
            raise ValueError("Snap ID must be non-negative")
        
        # Find the most recent update for this index with snap_count <= snap_id
        result_value = 0  # Default value
        
        for snap_count, update_index, value in self.updates:
            if update_index == index and snap_count <= snap_id:
                result_value = value  # Keep updating to get the most recent value
        
        return result_value


class TestSnapArray:
    """
    Test Suite for SnapArray - Focus on Storage Strengthening
    
    Following Laws of Nature Principles:
    - Law of Limited Working Memory: Test categories within 7±2
    - Law of Chunking: Tests grouped by functionality
    - Law of Sequential Processing: Tests progress from simple to complex
    """
    
    # CATEGORY 1: INITIALIZATION TESTS
    def test_snap_array_initialization(self):
        """Test snap array creation with different lengths"""
        snap_arr = SnapArray(5)
        assert snap_arr.length == 5
        assert snap_arr.snap_count == 0
        assert snap_arr.updates == []
    
    def test_invalid_initialization(self):
        """Test invalid initialization parameters"""
        with pytest.raises(ValueError):
            SnapArray(0)
        
        with pytest.raises(ValueError):
            SnapArray(-1)
    
    # CATEGORY 2: BASIC OPERATIONS
    def test_single_put_and_get(self):
        """Test basic put and get operations"""
        snap_arr = SnapArray(3)
        
        # Put value before any snapshot
        snap_arr.put(0, 5)
        
        # Create first snapshot
        snap_id = snap_arr.snap()
        assert snap_id == 0
        
        # Get value from snapshot
        assert snap_arr.get(0, 0) == 5
        assert snap_arr.get(1, 0) == 0  # Default value
        assert snap_arr.get(2, 0) == 0  # Default value
    
    def test_multiple_puts_same_index(self):
        """Test multiple puts to same index in same snapshot"""
        snap_arr = SnapArray(2)
        
        snap_arr.put(0, 10)
        snap_arr.put(0, 20)  # Overwrite previous value
        
        snap_id = snap_arr.snap()
        assert snap_arr.get(0, snap_id) == 20  # Latest value
    
    def test_default_values(self):
        """Test getting default values from empty snapshots"""
        snap_arr = SnapArray(3)
        
        snap_id = snap_arr.snap()  # Empty snapshot
        
        # All indices should return 0
        for i in range(3):
            assert snap_arr.get(i, snap_id) == 0
    
    # CATEGORY 3: SNAPSHOT BEHAVIOR
    def test_multiple_snapshots(self):
        """Test creating multiple snapshots"""
        snap_arr = SnapArray(2)
        
        # First snapshot
        snap_arr.put(0, 1)
        snap_id_0 = snap_arr.snap()
        assert snap_id_0 == 0
        
        # Second snapshot
        snap_arr.put(0, 2)
        snap_arr.put(1, 10)
        snap_id_1 = snap_arr.snap()
        assert snap_id_1 == 1
        
        # Third snapshot
        snap_arr.put(1, 20)
        snap_id_2 = snap_arr.snap()
        assert snap_id_2 == 2
        
        # Verify all snapshots
        assert snap_arr.get(0, 0) == 1
        assert snap_arr.get(1, 0) == 0
        
        assert snap_arr.get(0, 1) == 2
        assert snap_arr.get(1, 1) == 10
        
        assert snap_arr.get(0, 2) == 2  # Value persists
        assert snap_arr.get(1, 2) == 20
    
    def test_get_from_past_snapshots(self):
        """Test getting values from earlier snapshots"""
        snap_arr = SnapArray(1)
        
        # Build history
        snap_arr.put(0, 100)
        snap_0 = snap_arr.snap()
        
        snap_arr.put(0, 200)
        snap_1 = snap_arr.snap()
        
        snap_arr.put(0, 300)
        snap_2 = snap_arr.snap()
        
        # Get from different snapshots
        assert snap_arr.get(0, snap_0) == 100
        assert snap_arr.get(0, snap_1) == 200
        assert snap_arr.get(0, snap_2) == 300
    
    # CATEGORY 4: EDGE CASES
    def test_get_invalid_indices(self):
        """Test getting from invalid indices"""
        snap_arr = SnapArray(3)
        snap_id = snap_arr.snap()
        
        with pytest.raises(IndexError):
            snap_arr.get(-1, snap_id)
        
        with pytest.raises(IndexError):
            snap_arr.get(3, snap_id)
    
    def test_put_invalid_indices(self):
        """Test putting to invalid indices"""
        snap_arr = SnapArray(3)
        
        with pytest.raises(IndexError):
            snap_arr.put(-1, 5)
        
        with pytest.raises(IndexError):
            snap_arr.put(3, 5)
    
    def test_get_invalid_snap_id(self):
        """Test getting with invalid snap IDs"""
        snap_arr = SnapArray(1)
        
        with pytest.raises(ValueError):
            snap_arr.get(0, -1)
    
    def test_get_future_snap_id(self):
        """Test getting from future (non-existent) snap IDs"""
        snap_arr = SnapArray(1)
        
        snap_arr.put(0, 42)
        current_snap = snap_arr.snap()
        
        # Getting from future snap_id should find most recent value
        assert snap_arr.get(0, current_snap + 10) == 42
    
    # CATEGORY 5: COMPLEX SCENARIOS
    def test_interleaved_operations(self):
        """Test complex sequence of puts, gets, and snaps"""
        snap_arr = SnapArray(3)
        
        # Initial puts
        snap_arr.put(0, 1)
        snap_arr.put(1, 2)
        snap_0 = snap_arr.snap()
        
        # Update and check
        snap_arr.put(0, 10)
        assert snap_arr.get(0, snap_0) == 1  # Old value
        
        snap_1 = snap_arr.snap()
        assert snap_arr.get(0, snap_1) == 10  # New value
        assert snap_arr.get(1, snap_1) == 2   # Unchanged
        
        # More updates
        snap_arr.put(2, 100)
        snap_arr.put(1, 20)
        snap_2 = snap_arr.snap()
        
        # Verify final state
        assert snap_arr.get(0, snap_2) == 10   # Still 10
        assert snap_arr.get(1, snap_2) == 20   # Updated
        assert snap_arr.get(2, snap_2) == 100  # New value


if __name__ == "__main__":
    test_suite = TestSnapArray()
    
    print("SnapArray Test Suite")
    print("Storage Strengthening Focus - Laws of Nature Design")
    print("=" * 65)
    
    # Test categories for storage strengthening
    test_categories = [
        ("Initialization Tests", [
            "test_snap_array_initialization",
            "test_invalid_initialization"
        ]),
        ("Basic Operations", [
            "test_single_put_and_get",
            "test_multiple_puts_same_index",
            "test_default_values"
        ]),
        ("Snapshot Behavior", [
            "test_multiple_snapshots",
            "test_get_from_past_snapshots"
        ]),
        ("Edge Cases", [
            "test_get_invalid_indices",
            "test_put_invalid_indices",
            "test_get_invalid_snap_id",
            "test_get_future_snap_id"
        ]),
        ("Complex Scenarios", [
            "test_interleaved_operations"
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
            total_tests += 1
    
    print("\n" + "=" * 65)
    print(f"Test Results: {total_passed}/{total_tests} passed")
    print("\nStorage Strengthening Principles Applied:")
    print("• Progressive complexity from basic to advanced scenarios")
    print("• Focus on understanding snapshot behavior through testing")
    print("• Comprehensive edge case coverage")
    print("• Clear visualization of data structure operations")
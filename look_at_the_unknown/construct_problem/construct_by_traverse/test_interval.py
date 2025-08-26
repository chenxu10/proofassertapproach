import heapq
from typing import List


def canAttendMeetings(intervals: List[List[int]]) -> bool:
    """
    Determine if a person can attend all meetings without conflicts.
    
    Args:
        intervals: List of [start_time, end_time] for each meeting
    
    Returns:
        True if all meetings can be attended, False if there are conflicts
    """
    if not intervals or len(intervals) <= 1:
        return True
    
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    # Check for overlaps
    for i in range(1, len(intervals)):
        # If current meeting starts before previous meeting ends, there's a conflict
        if intervals[i][0] < intervals[i-1][1]:
            return False
    
    return True


def canAttendMeetingsHeap(intervals: List[List[int]]) -> bool:
    """
    Alternative heap-based solution for meeting scheduling problem.
    
    CONNECTION TO K-CLOSEST PROBLEM:
    - Both problems involve processing collections of 2D data points
    - K-closest uses heap to find minimum distances from origin
    - This problem uses heap to track meeting end times for conflict detection
    - Both leverage heap's ability to maintain ordered access to extremal values
    
    HEAP APPROACH LEVERAGED:
    - Min-heap maintains earliest ending meeting at top
    - Similar to how K-closest heap maintains closest points at top
    - Heap automatically sorts by priority (end time vs distance)
    - Pop operations give us the "next most important" element
    - Push operations maintain heap invariant efficiently
    
    ALGORITHM:
    1. Sort intervals by start time (like sorting points by some criteria)
    2. Use min-heap to track active meeting end times
    3. For each meeting, remove all ended meetings from heap
    4. Check if any active meeting conflicts with current meeting
    5. Add current meeting's end time to heap
    
    Args:
        intervals: List of [start_time, end_time] for each meeting
    
    Returns:
        True if all meetings can be attended, False if there are conflicts
    """
    if not intervals or len(intervals) <= 1:
        return True
    
    intervals.sort(key=lambda x: x[0])
    
    active_meetings = []
    
    def pop_last_round_end_meeting(active_meetings, start):
        while active_meetings and active_meetings[0] <= start:
            heapq.heappop(active_meetings)
        return

    def find_conflict_if_active_meeting_heap_not_none(active_meetings):
        if active_meetings:
            return False

    for start, end in intervals:  #[[2,3],[6,9]]
        pop_last_round_end_meeting(active_meetings, start)
        
        if active_meetings:
            return False
        
        heapq.heappush(active_meetings, end) # [3]
    
    return True






def test_canAttendMeetings_no_conflict():
    """Test case with no meeting conflicts"""
    intervals = [[0, 30], [60, 90], [120, 150]]
    assert canAttendMeetingsHeap(intervals) == True


def test_canAttendMeetings_with_conflict():
    """Test case with meeting conflicts"""
    intervals = [[0, 30], [15, 45], [60, 90]]
    assert canAttendMeetingsHeap(intervals) == False


def test_canAttendMeetings_adjacent_meetings():
    """Test case with adjacent meetings (no conflict)"""
    intervals = [[0, 30], [30, 60], [60, 90]]
    assert canAttendMeetings(intervals) == True


def test_canAttendMeetings_empty_list():
    """Test case with empty meeting list"""
    intervals = []
    assert canAttendMeetings(intervals) == True


def test_canAttendMeetings_single_meeting():
    """Test case with single meeting"""
    intervals = [[10, 20]]
    assert canAttendMeetings(intervals) == True


def test_canAttendMeetings_overlapping_start():
    """Test case where one meeting starts when another ends"""
    intervals = [[5, 10], [10, 15]]
    assert canAttendMeetings(intervals) == True


def test_canAttendMeetings_multiple_conflicts():
    """Test case with multiple overlapping meetings"""
    intervals = [[7, 10], [2, 4], [8, 12], [1, 5]]
    assert canAttendMeetings(intervals) == False


def test_canAttendMeetings_unsorted_input():
    """Test case with unsorted input intervals"""
    intervals = [[9, 10], [4, 9], [4, 17]]
    assert canAttendMeetings(intervals) == False


def test_canAttendMeetings_same_time():
    """Test case with meetings at exactly same time"""
    intervals = [[1, 5], [1, 5]]
    assert canAttendMeetings(intervals) == False


def test_canAttendMeetings_nested_meetings():
    """Test case with one meeting inside another"""
    intervals = [[1, 10], [3, 7]]
    assert canAttendMeetings(intervals) == False


def test_canAttendMeetings_back_to_back():
    """Test case with back-to-back meetings (valid)"""
    intervals = [[1, 3], [3, 6], [6, 8], [8, 10]]
    assert canAttendMeetings(intervals) == True


def test_canAttendMeetings_large_gaps():
    """Test case with large gaps between meetings"""
    intervals = [[1, 2], [100, 200], [1000, 2000]]
    assert canAttendMeetings(intervals) == True


def test_canAttendMeetings_reverse_order():
    """Test case with intervals in reverse chronological order"""
    intervals = [[50, 60], [30, 40], [10, 20]]
    assert canAttendMeetings(intervals) == True


def test_heap_solution_equivalence():
    """Test that heap solution gives same results as sorting solution"""
    test_cases = [
        [[0, 30], [60, 90], [120, 150]],  # no conflict
        [[0, 30], [15, 45], [60, 90]],    # conflict
        [[0, 30], [30, 60], [60, 90]],    # adjacent
        [],                               # empty
        [[10, 20]],                      # single
        [[5, 10], [10, 15]],             # touching
        [[7, 10], [2, 4], [8, 12], [1, 5]], # multiple conflicts
        [[9, 10], [4, 9], [4, 17]],      # unsorted with conflict
        [[1, 5], [1, 5]],                # same time
        [[1, 10], [3, 7]],               # nested
        [[1, 3], [3, 6], [6, 8], [8, 10]], # back to back
        [[50, 60], [30, 40], [10, 20]]   # reverse order
    ]
    
    for intervals in test_cases:
        original_result = canAttendMeetings(intervals.copy())
        heap_result = canAttendMeetingsHeap(intervals.copy())
        assert original_result == heap_result, f"Results differ for {intervals}: original={original_result}, heap={heap_result}"


if __name__ == "__main__":
    test_canAttendMeetings_no_conflict()
    test_canAttendMeetings_with_conflict()
    test_canAttendMeetings_adjacent_meetings()
    test_canAttendMeetings_empty_list()
    test_canAttendMeetings_single_meeting()
    test_canAttendMeetings_overlapping_start()
    test_canAttendMeetings_multiple_conflicts()
    test_canAttendMeetings_unsorted_input()
    test_canAttendMeetings_same_time()
    test_canAttendMeetings_nested_meetings()
    test_canAttendMeetings_back_to_back()
    test_canAttendMeetings_large_gaps()
    test_canAttendMeetings_reverse_order()
    test_heap_solution_equivalence()
    print("All tests passed!")
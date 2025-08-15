import heapq
import math
from typing import List


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Find the k closest points to the origin using a min-heap.
    
    Args:
        points: List of [x, y] coordinates
        k: Number of closest points to return
    
    Returns:
        List of k closest points to origin
   
    Key property of MinHeap: Parent Node <= Children Node

    assert nums[i] <= nums[2*i+1] and nums[2*i+2]
    """
    # Create heap with (distance, point) tuples

    heap = []
    for x, y in points:
        distance = x ** 2 + y ** 2
        heapq.heappush(heap, (distance,(x,y)))

    result = heapq.nsmallest(k, heap)
    result = [[p[0],p[1]] for d, p in result]
    return result


def test_kClosest_basic():
    """Test basic functionality"""
    points = [[1, 1], [2, 2], [3, 3]]
    k = 2
    result = kClosest(points, k)
    expected = [[1, 1], [2, 2]]
    assert result == expected


def test_kClosest_example1():
    """Test example 1 from problem"""
    points = [[1, 1], [2, 2], [3, 3]]
    k = 2
    result = kClosest(points, k)
    assert len(result) == 2
    assert [1, 1] in result
    assert [2, 2] in result


def test_kClosest_example2():
    """Test example 2 from problem"""
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    result = kClosest(points, k)
    assert len(result) == 2
    # Check distances: [3,3] = 18, [5,-1] = 26, [-2,4] = 20
    assert [3, 3] in result
    assert [-2, 4] in result


def test_kClosest_single_point():
    """Test with single point"""
    points = [[0, 1]]
    k = 1
    result = kClosest(points, k)
    assert result == [[0, 1]]


def test_kClosest_origin_point():
    """Test with point at origin"""
    points = [[0, 0], [3, 4], [1, 1]]
    k = 1
    result = kClosest(points, k)
    assert result == [[0, 0]]


def test_kClosest_negative_coordinates():
    """Test with negative coordinates"""
    points = [[-1, -1], [1, 1], [-2, -2], [2, 2]]
    k = 2
    result = kClosest(points, k)
    assert len(result) == 2
    # [-1,-1] and [1,1] both have distance 2, which is smallest
    assert [-1, -1] in result
    assert [1, 1] in result


def test_kClosest_all_points():
    """Test when k equals number of points"""
    points = [[1, 0], [0, 1], [2, 0]]
    k = 3
    result = kClosest(points, k)
    assert len(result) == 3
    assert set(map(tuple, result)) == set(map(tuple, points))


def test_kClosest_large_coordinates():
    """Test with larger coordinates"""
    points = [[10, 10], [1, 1], [5, 5], [2, 2]]
    k = 2
    result = kClosest(points, k)
    assert len(result) == 2
    assert [1, 1] in result
    assert [2, 2] in result


def test_kClosest_equal_distances():
    """Test with points having equal distances"""
    points = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    k = 2
    result = kClosest(points, k)
    assert len(result) == 2
    # All points have distance 1, any 2 are valid


if __name__ == "__main__":
    test_kClosest_basic()
    test_kClosest_example1()
    test_kClosest_example2()
    test_kClosest_single_point()
    test_kClosest_origin_point()
    test_kClosest_negative_coordinates()
    test_kClosest_all_points()
    test_kClosest_large_coordinates()
    test_kClosest_equal_distances()
    print("All tests passed!")
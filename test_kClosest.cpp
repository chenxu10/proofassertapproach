#include <iostream>
#include <vector>
#include <queue>
#include <cassert>
#include <algorithm>

using namespace std;

/**
 * Find the k closest points to the origin using a min-heap.
 * 
 * Args:
 *     points: Vector of [x, y] coordinates
 *     k: Number of closest points to return
 * 
 * Returns:
 *     Vector of k closest points to origin
 */
vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    // Create min-heap with (distance, point) pairs
    priority_queue<pair<int, vector<int>>, vector<pair<int, vector<int>>>, greater<pair<int, vector<int>>>> heap;
    
    for (int i = 0; i < points.size(); i++) {
        int x = points[i][0];
        int y = points[i][1];
        int distance = x * x + y * y;  // No need for sqrt since we're comparing
        heap.push({distance, {x, y}});
        
        // Loop invariant: heap property is maintained after each insertion
        // The heap should contain exactly (i+1) elements
        assert(heap.size() == i + 1);
    }
    
    vector<vector<int>> result;
    for (int i = 0; i < k && !heap.empty(); i++) {
        auto top = heap.top();
        heap.pop();
        result.push_back({top.second[0], top.second[1]});
    }
    
    return result;
}

/**
 * Test basic functionality
 */
void test_kClosest_basic() {
    cout << "Testing basic functionality..." << endl;
    
    vector<vector<int>> points = {{1, 1}, {2, 2}, {3, 3}};
    int k = 2;
    vector<vector<int>> result = kClosest(points, k);
    vector<vector<int>> expected = {{1, 1}, {2, 2}};
    
    // Verify result size
    assert(result.size() == expected.size());
    
    // Verify contents (order matters since we're using min-heap)
    for (int i = 0; i < result.size(); i++) {
        assert(result[i].size() == 2);
        assert(result[i][0] == expected[i][0]);
        assert(result[i][1] == expected[i][1]);
    }
    
    cout << "✓ Test passed: Basic kClosest functionality" << endl;
    
    // Print result for verification
    cout << "Result: [";
    for (int i = 0; i < result.size(); i++) {
        cout << "[" << result[i][0] << ", " << result[i][1] << "]";
        if (i < result.size() - 1) cout << ", ";
    }
    cout << "]" << endl;
}

int main() {
    cout << "Running k-Closest Points Test (C++ Version)" << endl;
    cout << "===========================================" << endl;
    
    try {
        test_kClosest_basic();
        cout << "\n🎉 All tests passed!" << endl;
    } catch (const exception& e) {
        cout << "❌ Test failed: " << e.what() << endl;
        return 1;
    }
    
    return 0;
}
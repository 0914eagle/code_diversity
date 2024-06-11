def maximum(arr, k):
    
    # Time Complexity: O(nlogk)
    # Space Complexity: O(k)
    # 1. Use a heap to store the k largest numbers.
    # 2. Iterate through the array and add each number to the heap.
    # 3. If the heap size is greater than k, remove the smallest number.
    # 4. Return the heap as a list.
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return list(heap)
/LeetCode/Easy/Python3/binary-tree-level-order-traversal.py
#
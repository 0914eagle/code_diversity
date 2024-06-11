def maximum(arr, k):
    
    # Time: O(nlogk)
    # Space: O(k)
    # 1. Use a min heap to keep track of the k largest elements in the array.
    # 2. Iterate through the array and insert each element into the min heap.
    # 3. If the size of the min heap exceeds k, remove the smallest element from the min heap.
    # 4. After iterating through the array, the min heap will contain the k largest elements in the array.
    # 5. Return the sorted list of the k largest elements in the array.
    min_heap = []
    for num in arr:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return sorted(min_heap)



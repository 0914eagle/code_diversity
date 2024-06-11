def maximum(arr, k):
    
    # Time: O(nlogk)
    # Space: O(k)
    # 1. Use a min heap to store the k largest numbers
    # 2. If the current number is larger than the smallest number in the heap,
    #    pop the smallest number and push the current number into the heap
    # 3. After the loop, the heap will contain the k largest numbers
    # 4. Sort the heap and return the result
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return sorted(heap)



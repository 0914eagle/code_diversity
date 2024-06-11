def maximum(arr, k):
    
    # Time: O(nlogk)
    # Space: O(k)
    if k == 0:
        return []
    if k == len(arr):
        return sorted(arr)
    heap = []
    for i in range(len(arr)):
        heapq.heappush(heap, arr[i])
        if len(heap) > k:
            heapq.heappop(heap)
    return sorted(heap, reverse=True)



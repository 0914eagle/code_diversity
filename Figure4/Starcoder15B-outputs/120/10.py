def maximum(arr, k):
    
    # Time: O(nlogk)
    # Space: O(k)
    if not arr:
        return []
    if k == len(arr):
        return sorted(arr)
    heap = []
    for i in range(k):
        heapq.heappush(heap, arr[i])
    for i in range(k, len(arr)):
        if arr[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, arr[i])
    return sorted(heap)


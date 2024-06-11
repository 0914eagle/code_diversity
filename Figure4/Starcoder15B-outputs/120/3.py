def maximum(arr, k):
    
    # Time: O(nlogk)
    # Space: O(k)
    pq = []
    for i in range(len(arr)):
        heapq.heappush(pq, arr[i])
        if len(pq) > k:
            heapq.heappop(pq)
    return sorted(pq, reverse=True)



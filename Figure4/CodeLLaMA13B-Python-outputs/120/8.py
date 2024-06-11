def maximum(arr, k):
    
    heap = []
    for i in range(k):
        heapq.heappush(heap, (arr[i], i))
    for i in range(k, len(arr)):
        if arr[i] > heap[0][0]:
            heapq.heappop(heap)
            heapq.heappush(heap, (arr[i], i))
    res = []
    for _ in range(k):
        res.append(heapq.heappop(heap)[0])
    return res


if
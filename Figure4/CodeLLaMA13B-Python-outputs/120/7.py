def maximum(arr, k):
    
    heap = []
    for i in range(k):
        heapq.heappush(heap, (arr[i], i))
    for i in range(k, len(arr)):
        if arr[i] > heap[0][0]:
            heapq.heappop(heap)
            heapq.heappush(heap, (arr[i], i))
    return [arr[i] for _, i in heap]


if
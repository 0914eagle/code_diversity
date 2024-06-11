def maximum(arr, k):
    
    if k == 0:
        return []
    if k == 1:
        return [max(arr)]
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
/leetcode/python/100_same_tree.py
#
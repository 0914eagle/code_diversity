def maximum(arr, k):
    
    if k == 0:
        return []
    if k == 1:
        return [max(arr)]
    if k == len(arr):
        return sorted(arr)

    # 1. Use a heap to store the k largest elements.
    # 2. Iterate through the array and compare each element with the smallest
    #    element in the heap. If the element is larger than the smallest element,
    #    remove the smallest element and add the element to the heap.
    # 3. Return the sorted list of the heap.
    heap = []
    for i in range(k):
        heapq.heappush(heap, arr[i])
    for i in range(k, len(arr)):
        if arr[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, arr[i])
    return sorted(heap)



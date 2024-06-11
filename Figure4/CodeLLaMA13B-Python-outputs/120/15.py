def maximum(arr, k):
    
    heap = []
    for num in arr:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
    return heap


if __name__ == "__main__":
    arr = [-3, -4, 5]
    k = 3

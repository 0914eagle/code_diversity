
import heapq

def combine_ingredients(N, values):
    heap = [(-value, value) for value in values]
    heapq.heapify(heap)
    
    for _ in range(N - 1):
        x = heapq.heappop(heap)[1]
        y = heapq.heappop(heap)[1]
        new_value = (x + y) / 2
        heapq.heappush(heap, (-new_value, new_value))
    
    return heap[0][1]

if __name__ == "__main__":
    N = int(input())
    values = list(map(int, input().split()))
    
    result = combine_ingredients(N, values)
    print(result)

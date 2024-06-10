
import heapq

def combine_ingredients(N, values):
    max_value = 0
    heap = [(-value, value) for value in values]
    heapq.heapify(heap)
    
    for _ in range(N - 1):
        x, y = heapq.heappop(heap)[1], heapq.heappop(heap)[1]
        new_value = (x + y) / 2
        max_value = max(max_value, new_value)
        heapq.heappush(heap, (-new_value, new_value))
    
    return max_value

if __name__ == "__main__":
    N = int(input())
    values = list(map(int, input().split()))
    result = combine_ingredients(N, values)
    print(result)


import heapq

def combine_ingredients(N, values):
    pq = [(-value, value) for value in values]
    heapq.heapify(pq)
    
    while len(pq) > 1:
        x = heapq.heappop(pq)[1]
        y = heapq.heappop(pq)[1]
        new_value = (x + y) / 2
        heapq.heappush(pq, (-new_value, new_value))
    
    return pq[0][1]

if __name__ == "__main__":
    N = int(input())
    values = list(map(int, input().split()))
    
    result = combine_ingredients(N, values)
    print(result)

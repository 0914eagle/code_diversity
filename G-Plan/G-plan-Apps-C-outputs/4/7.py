
import heapq

def find_min_time(n, levels):
    total_time = 0
    items = [0] * (n + 1)
    
    for i in range(n):
        shortcut_item, shortcut_time, *completion_times = levels[i]
        best_time = min(completion_times)
        items[i + 1] = best_time
        total_time += best_time
    
    return total_time

if __name__ == "__main__":
    n = int(input())
    levels = [list(map(int, input().split())) for _ in range(n)]
    
    result = find_min_time(n, levels)
    print(result)

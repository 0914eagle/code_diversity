
import heapq

def find_minimum_time(n, levels):
    total_time = 0
    items = [0] * (n + 1)
    
    for i in range(n):
        shortcut_item, shortcut_time, *completion_times = levels[i]
        best_item = min(range(n + 1), key=lambda x: completion_times[x])
        
        if completion_times[shortcut_item] <= completion_times[best_item]:
            best_item = shortcut_item
        
        total_time += completion_times[best_item]
        items[i] = best_item
    
    return total_time

if __name__ == "__main__":
    n = int(input())
    levels = [list(map(int, input().split())) for _ in range(n)]
    
    result = find_minimum_time(n, levels)
    print(result)


import heapq

def find_shortest_completion_time(levels, items):
    min_time = float('inf')
    for i in range(len(items)):
        if items[i] < min_time:
            min_time = items[i]
    return min_time

def min_time_to_beat_all_levels(n, level_data):
    total_time = 0
    for i in range(n):
        shortcut_item, shortcut_time, *completion_times = level_data[i]
        best_time = find_shortest_completion_time(n+1, completion_times)
        if completion_times[shortcut_item] < best_time:
            best_time = completion_times[shortcut_item]
        total_time += best_time
    return total_time

if __name__ == "__main__":
    n = int(input())
    level_data = [list(map(int, input().split())) for _ in range(n)]
    print(min_time_to_beat_all_levels(n, level_data))

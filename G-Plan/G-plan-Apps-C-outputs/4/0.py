
import heapq

def find_shortest_completion_time(levels, items):
    min_completion_times = []
    for level in levels:
        shortcut_item, shortcut_time, *completion_times = level
        min_completion_time = min(completion_times[shortcut_item], shortcut_time)
        min_completion_times.append(min_completion_time)
    return min_completion_times

def min_time_to_beat(levels, items):
    min_completion_times = find_shortest_completion_time(levels, items)
    total_time = sum(min_completion_times)
    return total_time

if __name__ == "__main__":
    n = int(input())
    levels = [list(map(int, input().split())) for _ in range(n)]
    items = [level[1:] for level in levels]
    print(min_time_to_beat(levels, items))

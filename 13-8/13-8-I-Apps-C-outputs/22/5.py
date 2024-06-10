
import math

def get_tide_height(t, a):
    return 0.5 * a * (math.cos(t * 2 * math.pi / 12) + 1)

def is_safe_to_enter_square(square_height, tide_height):
    return abs(square_height - tide_height) <= 1

def get_shortest_path_length(graph, start, end):
    visited = set()
    queue = [(0, start)]
    while queue:
        dist, curr = queue.pop(0)
        if curr == end:
            return dist
        if curr in visited:
            continue
        visited.add(curr)
        for neighbor in graph[curr]:
            queue.append((dist + 1, neighbor))
    return -1

def get_max_distance_from_home(height_map, speed, width, height):
    graph = {}
    for y in range(height):
        for x in range(width):
            graph[(x, y)] = []
            if x > 0:
                graph[(x, y)].append((x - 1, y))
            if x < width - 1:
                graph[(x, y)].append((x + 1, y))
            if y > 0:
                graph[(x, y)].append((x, y - 1))
            if y < height - 1:
                graph[(x, y)].append((x, y + 1))

    tide_height = get_tide_height(0, a)
    max_distance = 0
    for y in range(height):
        for x in range(width):
            if is_safe_to_enter_square(height_map[y][x], tide_height):
                distance = get_shortest_path_length(graph, (x, y), (width - 1, height - 1))
                if distance > 0 and distance * speed > max_distance:
                    max_distance = distance * speed

    return max_distance

def main():
    a, speed = map(float, input().split())
    width, height = map(int, input().split())
    x, y = map(int, input().split())
    height_map = []
    for _ in range(height):
        height_map.append(list(map(int, input().split())))
    print(get_max_distance_from_home(height_map, speed, width, height))

if __name__ == '__main__':
    main()


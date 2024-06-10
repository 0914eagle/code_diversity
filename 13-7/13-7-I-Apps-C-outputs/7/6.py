
def get_min_turns(intersections, alice_intersection, bob_intersection):
    # Initialize a dictionary to store the distances from each intersection to the leaning tower
    distances = {}
    for i in range(len(intersections)):
        distances[i] = float('inf')
    distances[alice_intersection] = 0

    # Breadth-first search to find the shortest distance from each intersection to the leaning tower
    queue = [alice_intersection]
    while queue:
        current_intersection = queue.pop(0)
        for next_intersection in intersections[current_intersection]:
            if next_intersection not in distances or distances[next_intersection] > distances[current_intersection] + 1:
                distances[next_intersection] = distances[current_intersection] + 1
                queue.append(next_intersection)

    # Return the minimum distance from either Alice or Bob's current intersection to the leaning tower
    return min(distances[alice_intersection], distances[bob_intersection])

def main():
    n, alice_intersection, bob_intersection = map(int, input().split())
    intersections = [[] for _ in range(n)]
    for _ in range(n):
        l, r, t = map(int, input().split())
        intersections[l].append(r)
        intersections[r].append(l)
    print(get_min_turns(intersections, alice_intersection, bob_intersection))

if __name__ == '__main__':
    main()


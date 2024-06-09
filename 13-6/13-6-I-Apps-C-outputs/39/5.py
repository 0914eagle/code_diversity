
def get_next_island(current_island, bridges, n):
    # Find the island directly adjacent to the current island
    for i in range(n):
        if current_island in bridges[i]:
            return i

def rearrange_statues(statues, bridges, n):
    # Initialize the current island and the desired island
    current_island = 0
    desired_island = 1

    # Loop through each statue and move it to the desired island
    for i in range(n):
        # Find the island directly adjacent to the current island
        next_island = get_next_island(current_island, bridges, n)

        # Move the statue from the current island to the next island
        statues[next_island] = statues[current_island]
        statues[current_island] = 0

        # Update the current and desired islands
        current_island = next_island
        desired_island = (desired_island + 1) % n

    # Check if the statues are in the desired order
    return statues == desired_island

def main():
    n = int(input())
    statues = list(map(int, input().split()))
    bridges = [[] for _ in range(n)]
    for i in range(n):
        bridges[i].append((i + 1) % n)
        bridges[i].append((i - 1) % n)
    print("YES" if rearrange_statues(statues, bridges, n) else "NO")

if __name__ == '__main__':
    main()


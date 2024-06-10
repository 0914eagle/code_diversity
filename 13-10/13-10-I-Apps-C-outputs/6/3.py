
def solve(A, H, n, m, passages):
    # Initialize a graph to store the cave-system
    graph = {}
    for i in range(n):
        graph[i] = []
    
    # Add passages to the graph
    for e, b, a, h in passages:
        graph[e].append((b, a, h))
    
    # Initialize a queue to store the areas to visit
    queue = [1]
    
    # Initialize a dictionary to store the maximum health Unnar can have after visiting each area
    max_health = {1: H}
    
    # Loop through the areas in the graph
    while queue:
        current_area = queue.pop(0)
        for next_area, enemy_attack, enemy_health in graph[current_area]:
            # If Unnar has enough health to fight the enemy
            if max_health[current_area] >= enemy_attack:
                # Update the maximum health Unnar can have after fighting the enemy
                max_health[next_area] = max(max_health[current_area] - enemy_attack, enemy_health)
                # Add the next area to the queue
                queue.append(next_area)
    
    # If Unnar can't get to the last area, return 'Oh no'
    if max_health[n] == 0:
        return 'Oh no'
    # Otherwise, return the maximum health Unnar can have after getting to the last area
    else:
        return max_health[n]

def main():
    A, H, n, m = map(int, input().split())
    passages = []
    for i in range(m):
        e, b, a, h = map(int, input().split())
        passages.append((e, b, a, h))
    print(solve(A, H, n, m, passages))

if __name__ == '__main__':
    main()


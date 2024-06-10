
def get_input():
    A, H = map(int, input().split())
    n, m = map(int, input().split())
    passages = []
    for _ in range(m):
        e, b, a, h = map(int, input().split())
        passages.append((e, b, a, h))
    return A, H, n, m, passages

def solve(A, H, n, m, passages):
    # Initialize a dictionary to keep track of the enemies and their health points
    enemies = {i: h for i, _, _, h in passages}
    
    # Initialize a list to keep track of the areas that Unnar has visited
    visited = [1]
    
    # Initialize a variable to keep track of the maximum health Unnar can have
    max_health = H
    
    # Loop through the passages and visit each one
    for e, b, a, h in passages:
        if b in visited:
            # If the area Unnar is trying to reach has already been visited, skip this passage
            continue
        if A >= a:
            # If Unnar's attack points are greater than or equal to the enemy's attack points, fight the enemy
            enemies[b] -= A
            if enemies[b] <= 0:
                # If the enemy has no health points left, remove it from the dictionary
                del enemies[b]
            visited.append(b)
            if b == n:
                # If Unnar has reached the last area, update the maximum health
                max_health = max(max_health, H - enemies[b])
        else:
            # If Unnar's attack points are less than the enemy's attack points, skip this passage
            continue
    
    # If Unnar has not visited all the areas, output 'Oh no'
    if len(visited) < n:
        return "Oh no"
    
    # Otherwise, output the maximum health Unnar can have
    return max_health

def main():
    A, H, n, m, passages = get_input()
    print(solve(A, H, n, m, passages))

if __name__ == '__main__':
    main()


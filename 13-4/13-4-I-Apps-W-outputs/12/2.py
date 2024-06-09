
def find_walk(x, y, x1, y1, x2, y2, a, b, c, d):
    # Initialize the position of the cat
    pos = [x, y]
    
    # Initialize the number of steps left, right, up, and down
    left, right, up, down = a, b, c, d
    
    # Initialize the walk
    walk = []
    
    # While there are still steps left, right, up, and down
    while left + right + up + down > 0:
        # If there are steps left, add them to the walk
        if left > 0:
            walk.append("L")
            pos[0] -= 1
            left -= 1
        
        # If there are steps right, add them to the walk
        if right > 0:
            walk.append("R")
            pos[0] += 1
            right -= 1
        
        # If there are steps up, add them to the walk
        if up > 0:
            walk.append("U")
            pos[1] += 1
            up -= 1
        
        # If there are steps down, add them to the walk
        if down > 0:
            walk.append("D")
            pos[1] -= 1
            down -= 1
    
    # If the final position is within the allowed range, return the walk
    if x1 <= pos[0] <= x2 and y1 <= pos[1] <= y2:
        return "".join(walk)
    
    # Otherwise, return None
    return None

def main():
    # Read the input
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        x, y, x1, y1, x2, y2 = map(int, input().split())
        
        # Find the walk
        walk = find_walk(x, y, x1, y1, x2, y2, a, b, c, d)
        
        # Print the result
        if walk is None:
            print("NO")
        else:
            print("YES")
            print(walk)

if __name__ == '__main__':
    main()


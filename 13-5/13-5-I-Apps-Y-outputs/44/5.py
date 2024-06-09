
def can_reach_n1(n, m, d, c):
    # Initialize the array a as all 0s
    a = [0] * (n + 2)
    
    # Loop through each platform
    for i in range(m):
        # Get the length of the current platform
        length = c[i]
        
        # Loop through each cell in the platform
        for j in range(length):
            # Set the cell to the current platform index
            a[j + 1] = i + 1
    
    # Loop through each cell in the river
    for i in range(1, n + 1):
        # If the cell is not 0, check if it is reachable from the previous cell
        if a[i] != 0 and not is_reachable(a, i, d):
            # If it is not reachable, return False
            return False
    
    # If all cells are reachable, return True
    return True

def is_reachable(a, i, d):
    # If the cell is 0, return True
    if a[i] == 0:
        return True
    
    # Loop through each cell in the platform
    for j in range(i, min(i + d, len(a))):
        # If the cell is reachable, return True
        if a[j] == 0:
            return True
    
    # If all cells in the platform are not reachable, return False
    return False

def main():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    print("YES" if can_reach_n1(n, m, d, c) else "NO")

if __name__ == '__main__':
    main()


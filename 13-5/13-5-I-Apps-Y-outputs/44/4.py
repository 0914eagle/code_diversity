
def can_reach_n1(n, m, d, c):
    # Initialize the array a as all 0s
    a = [0] * (n + 2)
    
    # Set the first and last cells as 1, as they belong to platforms
    a[0] = 1
    a[n + 1] = 1
    
    # Loop through the platforms
    for i in range(m):
        # Get the length of the current platform
        length = c[i]
        
        # Loop through the cells of the current platform
        for j in range(length):
            # Set the current cell as the index of the current platform
            a[j + 1] = i + 1
    
    # Initialize the maximum distance of jump as d
    max_distance = d
    
    # Loop through the cells of the river
    for i in range(1, n + 1):
        # If the current cell is not 0, check if it is possible to jump to the next cell
        if a[i] != 0:
            # If the next cell is not 0 and the distance between the current cell and the next cell is less than or equal to the maximum distance, set the next cell as the current cell
            if a[i + 1] != 0 and i + d <= n + 1:
                a[i + d] = a[i]
        
        # If the current cell is 0, check if it is possible to jump to the previous cell
        else:
            # If the previous cell is not 0 and the distance between the current cell and the previous cell is less than or equal to the maximum distance, set the previous cell as the current cell
            if a[i - 1] != 0 and i - d >= 1:
                a[i - d] = 0
    
    # Return True if the last cell is 1, False otherwise
    return a[n + 1] == 1

def main():
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    print("YES" if can_reach_n1(n, m, d, c) else "NO")

if __name__ == '__main__':
    main()


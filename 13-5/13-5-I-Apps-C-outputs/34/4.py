
def get_min_heights(n, m, heights):
    # Initialize the minimum heights array
    min_heights = [1] * (n * m)
    
    # Loop through each intersection
    for i in range(n):
        for j in range(m):
            # Get the current height
            current_height = heights[i][j]
            
            # Get the minimum height for the current intersection
            min_height = 1
            for k in range(n):
                if k != i:
                    min_height = max(min_height, min_heights[k * m + j])
            for k in range(m):
                if k != j:
                    min_height = max(min_height, min_heights[i * m + k])
            
            # Update the minimum height for the current intersection
            min_heights[i * m + j] = min(current_height, min_height)
    
    return min_heights

def main():
    n, m = map(int, input().split())
    heights = []
    for i in range(n):
        heights.append(list(map(int, input().split())))
    min_heights = get_min_heights(n, m, heights)
    for i in range(n):
        print(*min_heights[i * m:(i + 1) * m])

if __name__ == '__main__':
    main()


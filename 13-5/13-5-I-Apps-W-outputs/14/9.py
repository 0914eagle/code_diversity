
def get_min_height(n, m):
    # Initialize a list to store the heights of the towers
    heights = []
    
    # Add the heights of the towers made with two-block pieces
    for i in range(1, n+1):
        heights.append(i*2)
    
    # Add the heights of the towers made with three-block pieces
    for i in range(1, m+1):
        heights.append(i*3)
    
    # Return the maximum height
    return max(heights)
    
def main():
    n, m = map(int, input().split())
    print(get_min_height(n, m))
    
if __name__ == '__main__':
    main()


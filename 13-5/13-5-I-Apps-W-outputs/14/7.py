
def get_tower_height(n, m):
    # Initialize a list to store the heights of the towers
    tower_heights = []
    
    # Add the heights of the towers made with two-block pieces
    for i in range(1, n + 1):
        tower_heights.append(i * 2)
    
    # Add the heights of the towers made with three-block pieces
    for i in range(1, m + 1):
        tower_heights.append(i * 3)
    
    # Return the maximum height in the list
    return max(tower_heights)

def main():
    n, m = map(int, input().split())
    print(get_tower_height(n, m))

if __name__ == '__main__':
    main()


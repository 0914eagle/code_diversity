
def get_tallest_tower(n, m):
    # Initialize a list to store the heights of the towers
    tower_heights = []
    
    # Add the heights of the towers made with two-block pieces
    for i in range(n):
        tower_heights.append(2 * i + 2)
    
    # Add the heights of the towers made with three-block pieces
    for i in range(m):
        tower_heights.append(3 * i + 3)
    
    # Return the tallest tower height
    return max(tower_heights)

def main():
    n, m = map(int, input().split())
    print(get_tallest_tower(n, m))

if __name__ == '__main__':
    main()


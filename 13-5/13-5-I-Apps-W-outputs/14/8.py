
def get_tallest_tower(n_two_blocks, m_three_blocks):
    # Initialize a list to store the heights of the towers
    tower_heights = []
    
    # Add the heights of the towers made with two blocks
    for i in range(1, n_two_blocks + 1):
        tower_heights.append(i * 2)
    
    # Add the heights of the towers made with three blocks
    for i in range(1, m_three_blocks + 1):
        tower_heights.append(i * 3)
    
    # Return the tallest tower height
    return max(tower_heights)

def main():
    n_two_blocks, m_three_blocks = map(int, input().split())
    print(get_tallest_tower(n_two_blocks, m_three_blocks))

if __name__ == '__main__':
    main()


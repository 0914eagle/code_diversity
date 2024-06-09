
def get_tower_heights(box_heights, tower_heights):
    # Initialize variables
    tower_1 = []
    tower_2 = []
    
    # Sort the box heights in descending order
    sorted_box_heights = sorted(box_heights, reverse=True)
    
    # Add the largest box height to the first tower
    tower_1.append(sorted_box_heights.pop())
    
    # Add the next two smallest box heights to the first tower
    tower_1.append(sorted_box_heights.pop())
    tower_1.append(sorted_box_heights.pop())
    
    # Add the remaining box heights to the second tower
    tower_2 = sorted_box_heights
    
    # Return the tower heights in order
    return tower_1, tower_2

def main():
    # Test case 1
    box_heights = [12, 8, 2, 4, 10, 3]
    tower_heights = [25, 14]
    expected_output = [12, 10, 3, 8, 4, 2]
    output = get_tower_heights(box_heights, tower_heights)
    assert output == expected_output
    
    # Test case 2
    box_heights = [12, 8, 2, 4, 10, 3]
    tower_heights = [25, 14]
    expected_output = [12, 10, 3, 8, 4, 2]
    output = get_tower_heights(box_heights, tower_heights)
    assert output == expected_output
    
    # Test case 3
    box_heights = [12, 8, 2, 4, 10, 3]
    tower_heights = [25, 14]
    expected_output = [12, 10, 3, 8, 4, 2]
    output = get_tower_heights(box_heights, tower_heights)
    assert output == expected_output
    
    print("All tests passed!")

if __name__ == '__main__':
    main()


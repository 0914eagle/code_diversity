
def get_number_of_blocks(volume, blocks):
    # Initialize variables
    number_of_blocks = 0
    current_volume = 0
    
    # Iterate through the blocks and add them to the tower until the volume exceeds the given volume
    for block in blocks:
        current_volume += block ** 3
        number_of_blocks += 1
        if current_volume > volume:
            break
    
    # Return the number of blocks and the current volume
    return number_of_blocks, current_volume

def get_maximum_volume_and_number_of_blocks(m):
    # Initialize variables
    maximum_volume = 0
    maximum_number_of_blocks = 0
    
    # Iterate through the possible values of X and find the maximum number of blocks and the maximum volume
    for x in range(1, m + 1):
        # Get the number of blocks and the current volume for the current value of X
        number_of_blocks, current_volume = get_number_of_blocks(x, range(1, x + 1))
        
        # If the current number of blocks is greater than the maximum number of blocks, update the maximum number of blocks and volume
        if number_of_blocks > maximum_number_of_blocks:
            maximum_number_of_blocks = number_of_blocks
            maximum_volume = current_volume
    
    # Return the maximum number of blocks and the maximum volume
    return maximum_number_of_blocks, maximum_volume

if __name__ == '__main__':
    m = int(input())
    number_of_blocks, maximum_volume = get_maximum_volume_and_number_of_blocks(m)
    print(number_of_blocks, maximum_volume)


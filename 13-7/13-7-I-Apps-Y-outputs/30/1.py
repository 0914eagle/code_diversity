
def get_sequence_element(position):
    # Initialize variables
    current_block_start = 1
    current_block_end = 1
    current_block_size = 1
    current_element = 1

    # Loop through the sequence
    while current_element <= position:
        # Calculate the current block size
        current_block_size = current_block_end - current_block_start + 1

        # Check if the current element is in the current block
        if current_element == position:
            # Return the current element
            return current_element
        elif current_element > position:
            # Calculate the previous block size
            previous_block_size = current_block_size - 1

            # Calculate the previous block start and end
            previous_block_start = current_block_start
            previous_block_end = current_block_end - 1

            # Update the current block start and end
            current_block_start = previous_block_start
            current_block_end = previous_block_end

            # Update the current block size
            current_block_size = previous_block_size

            # Update the current element
            current_element = current_element - previous_block_size
        else:
            # Calculate the next block start and end
            next_block_start = current_block_end + 1
            next_block_end = next_block_start + current_block_size - 1

            # Update the current block start and end
            current_block_start = next_block_start
            current_block_end = next_block_end

            # Update the current element
            current_element = current_element + current_block_size

    # Return the current element
    return current_element

def main():
    # Read the number of queries
    q = int(input())

    # Loop through the queries
    for i in range(q):
        # Read the query
        k = int(input())

        # Calculate the element at the position k
        element = get_sequence_element(k)

        # Print the element
        print(element)

if __name__ == '__main__':
    main()


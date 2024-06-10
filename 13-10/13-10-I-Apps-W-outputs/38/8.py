
def get_possible_placements(n, k):
    # Initialize a list to store the possible placements
    possible_placements = []
    
    # Iterate over each possible placement of the rooks
    for i in range(n):
        for j in range(n):
            # Check if the current placement is valid
            if valid_placement(i, j, n, k):
                # Add the current placement to the list of possible placements
                possible_placements.append((i, j))
    
    # Return the list of possible placements
    return possible_placements

def valid_placement(i, j, n, k):
    # Initialize a variable to store the number of pairs of rooks that attack each other
    num_attacking_pairs = 0
    
    # Iterate over each row
    for row in range(n):
        # Check if the current row is the same as the row of the current placement
        if row == i:
            # Iterate over each column
            for col in range(n):
                # Check if the current column is the same as the column of the current placement
                if col == j:
                    # Increment the number of pairs of rooks that attack each other
                    num_attacking_pairs += 1
    
    # Check if the number of pairs of rooks that attack each other is less than or equal to k
    return num_attacking_pairs <= k

def count_possible_placements(n, k):
    # Get the list of possible placements
    possible_placements = get_possible_placements(n, k)
    
    # Initialize a variable to store the count of possible placements
    count = 0
    
    # Iterate over each possible placement
    for placement in possible_placements:
        # Increment the count of possible placements
        count += 1
    
    # Return the count of possible placements
    return count

def main():
    # Read the input
    n, k = map(int, input().split())
    
    # Calculate the number of possible placements
    count = count_possible_placements(n, k)
    
    # Print the number of possible placements
    print(count % 998244353)

if __name__ == '__main__':
    main()


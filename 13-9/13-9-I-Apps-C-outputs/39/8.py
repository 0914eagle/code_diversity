
def get_expected_weight(n, m, a, w):
    # Initialize the expected weight of each picture
    expected_weight = [0] * n
    
    # Iterate over each visit
    for i in range(m):
        # Choose a picture randomly according to its weight
        picture_index = choose_picture(w)
        
        # If the chosen picture is liked by Nauuo, add 1 to its weight
        if a[picture_index] == 1:
            w[picture_index] += 1
        # Otherwise, subtract 1 from its weight
        else:
            w[picture_index] -= 1
        
        # Update the expected weight of the chosen picture
        expected_weight[picture_index] += w[picture_index] / (i + 1)
    
    # Return the expected weight of each picture
    return expected_weight

def choose_picture(w):
    # Generate a random number between 0 and the sum of all weights
    random_number = random.randint(0, sum(w))
    
    # Initialize the current weight to 0
    current_weight = 0
    
    # Iterate over each picture
    for i in range(len(w)):
        # If the current weight is less than the random number, choose the current picture
        if current_weight < random_number <= current_weight + w[i]:
            return i
        # Otherwise, update the current weight
        current_weight += w[i]
    
    # If no picture is chosen, return the last picture
    return len(w) - 1

def main():
    # Read the input
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))
    
    # Call the function to get the expected weight of each picture
    expected_weight = get_expected_weight(n, m, a, w)
    
    # Print the expected weight of each picture
    for i in range(n):
        print(expected_weight[i])

if __name__ == '__main__':
    main()


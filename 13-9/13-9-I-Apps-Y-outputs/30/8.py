
def get_dogs(A, B, C, D):
    # Calculate the number of aggressive minutes for each dog
    dog1_aggressive_minutes = A + B
    dog2_aggressive_minutes = C + D
    
    # Return the number of aggressive minutes for each dog
    return dog1_aggressive_minutes, dog2_aggressive_minutes

def get_attacking_dogs(dog1_aggressive_minutes, dog2_aggressive_minutes, P, M, G):
    # Initialize variables to keep track of the number of aggressive minutes for each dog
    dog1_aggressive_count = 0
    dog2_aggressive_count = 0
    
    # Loop through the minutes in the day
    for minute in range(1, 1000):
        # Check if the postman, milkman, and garbage man arrived at house 18
        if minute == P or minute == M or minute == G:
            # Check if the dogs are aggressive
            if dog1_aggressive_count < dog1_aggressive_minutes and dog2_aggressive_count < dog2_aggressive_minutes:
                # If both dogs are aggressive, return 'both'
                return 'both'
            elif dog1_aggressive_count < dog1_aggressive_minutes:
                # If only the first dog is aggressive, return 'one'
                return 'one'
            elif dog2_aggressive_count < dog2_aggressive_minutes:
                # If only the second dog is aggressive, return 'one'
                return 'one'
            else:
                # If neither dog is aggressive, return 'none'
                return 'none'
        # Increment the aggressive count for each dog
        dog1_aggressive_count += 1
        dog2_aggressive_count += 1
        # Reset the aggressive count for each dog if they are no longer aggressive
        if dog1_aggressive_count == dog1_aggressive_minutes:
            dog1_aggressive_count = 0
        if dog2_aggressive_count == dog2_aggressive_minutes:
            dog2_aggressive_count = 0
    
if __name__ == '__main__':
    # Get the input from the user
    A, B, C, D = map(int, input().split())
    P, M, G = map(int, input().split())
    
    # Call the get_dogs function to get the number of aggressive minutes for each dog
    dog1_aggressive_minutes, dog2_aggressive_minutes = get_dogs(A, B, C, D)
    
    # Call the get_attacking_dogs function to determine how many dogs attack each of the heroes
    print(get_attacking_dogs(dog1_aggressive_minutes, dog2_aggressive_minutes, P, M, G))


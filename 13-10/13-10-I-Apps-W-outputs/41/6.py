
def get_required_minutes(hamsters_list):
    # Find the number of hamsters that need to stand up
    num_hamsters_to_stand_up = len(hamsters_list) // 2
    
    # Count the number of hamsters that are already standing
    num_hamsters_standing = hamsters_list.count('X')
    
    # Calculate the difference between the number of hamsters that need to stand up and the number of hamsters that are already standing
    difference = abs(num_hamsters_to_stand_up - num_hamsters_standing)
    
    # Return the minimum number of minutes required to get the desired number of standing hamsters
    return difference

def get_desired_hamsters_position(hamsters_list):
    # Find the number of hamsters that need to stand up
    num_hamsters_to_stand_up = len(hamsters_list) // 2
    
    # Count the number of hamsters that are already standing
    num_hamsters_standing = hamsters_list.count('X')
    
    # Calculate the difference between the number of hamsters that need to stand up and the number of hamsters that are already standing
    difference = abs(num_hamsters_to_stand_up - num_hamsters_standing)
    
    # Create a list to store the desired hamsters' position
    desired_hamsters_position = []
    
    # Iterate through the hamsters' list and update the desired position for each hamster
    for i in range(len(hamsters_list)):
        if hamsters_list[i] == 'X':
            if difference > 0:
                desired_hamsters_position.append('x')
                difference -= 1
            else:
                desired_hamsters_position.append('X')
        else:
            desired_hamsters_position.append('X')
    
    # Return the desired hamsters' position
    return ''.join(desired_hamsters_position)

if __name__ == '__main__':
    # Read the number of hamsters and their position from stdin
    n = int(input())
    hamsters_list = input()
    
    # Call the functions to get the required minutes and the desired hamsters' position
    required_minutes = get_required_minutes(hamsters_list)
    desired_hamsters_position = get_desired_hamsters_position(hamsters_list)
    
    # Print the required minutes and the desired hamsters' position
    print(required_minutes)
    print(desired_hamsters_position)


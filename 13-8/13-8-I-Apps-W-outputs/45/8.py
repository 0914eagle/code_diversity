
def get_min_night_count(total_mass, bacteria_count=1):
    # Base case: if the total mass is 1, return 0 nights
    if total_mass == 1:
        return 0
    
    # Initialize variables
    night_count = 0
    current_mass = 1
    bacteria_count_list = [bacteria_count]
    
    # Loop until the total mass is reached
    while current_mass < total_mass:
        # Increment the night count
        night_count += 1
        
        # Split the bacteria
        bacteria_count_list = [bacteria_count_list[i] // 2 for i in range(len(bacteria_count_list))]
        
        # Increment the mass of each bacterium
        current_mass += sum(bacteria_count_list)
    
    # Return the minimum number of nights needed
    return night_count

def get_bacteria_split_counts(total_mass, night_count):
    # Initialize variables
    bacteria_count = 1
    current_mass = 1
    bacteria_split_counts = [0] * night_count
    
    # Loop until the total mass is reached
    while current_mass < total_mass:
        # Increment the mass of each bacterium
        current_mass += bacteria_count
        
        # Split the bacteria
        bacteria_count_list = [bacteria_count // 2 for i in range(bacteria_count)]
        bacteria_count = sum(bacteria_count_list)
        
        # Increment the split count for each night
        for i in range(night_count):
            bacteria_split_counts[i] += len(bacteria_count_list)
    
    # Return the bacteria split counts
    return bacteria_split_counts

def main():
    # Read the input
    test_cases = int(input())
    for _ in range(test_cases):
        total_mass = int(input())
        
        # Get the minimum number of nights needed
        night_count = get_min_night_count(total_mass)
        
        # Check if a solution exists
        if night_count == -1:
            print(-1)
        else:
            # Get the bacteria split counts
            bacteria_split_counts = get_bacteria_split_counts(total_mass, night_count)
            
            # Print the output
            print(night_count)
            print(" ".join(map(str, bacteria_split_counts)))

if __name__ == '__main__':
    main()


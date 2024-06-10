
def get_bacteria_split_count(n):
    # Initialize variables
    bacteria_count = 1
    bacteria_mass = 1
    night_count = 0
    split_count = []
    
    # Loop until the total mass is equal to n
    while bacteria_mass < n:
        # Split the bacteria
        bacteria_count += bacteria_count
        bacteria_mass += bacteria_count
        night_count += 1
        split_count.append(bacteria_count)
    
    # Return the minimum number of nights needed and the split count
    return night_count, split_count

def get_bacteria_split_count_v2(n):
    # Initialize variables
    bacteria_count = 1
    bacteria_mass = 1
    night_count = 0
    split_count = []
    
    # Loop until the total mass is equal to n
    while bacteria_mass < n:
        # Split the bacteria
        bacteria_count += bacteria_count
        bacteria_mass += bacteria_count
        night_count += 1
        split_count.append(bacteria_count)
    
    # Return the minimum number of nights needed and the split count
    return night_count, split_count

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        night_count, split_count = get_bacteria_split_count(n)
        print(night_count)
        print(" ".join(map(str, split_count)))


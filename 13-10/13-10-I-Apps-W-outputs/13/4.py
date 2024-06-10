
def get_number_of_partitions(a, l, r):
    # Initialize a list to store the partitions
    partitions = []
    
    # Iterate through all possible lengths of partitions
    for length in range(1, a + 1):
        # Get all possible partitions of length "length"
        partition_list = get_partitions(a, length)
        
        # Iterate through the partitions and check if they meet the requirements
        for partition in partition_list:
            # Check if the partition meets the requirements
            if meets_requirements(partition, l, r):
                # Add the partition to the list of partitions
                partitions.append(partition)
    
    # Return the number of partitions
    return len(partitions)

def get_partitions(a, length):
    # Initialize a list to store the partitions
    partitions = []
    
    # Base case: if the length of the partition is 1, return the number itself
    if length == 1:
        return [a]
    
    # Recursive case: get all possible partitions of the number - 1 with length = length - 1
    for partition in get_partitions(a - 1, length - 1):
        # Add the number to the partition
        partitions.append([a] + partition)
    
    # Return the list of partitions
    return partitions

def meets_requirements(partition, l, r):
    # Check if the partition meets the requirements
    for element in partition:
        # Check if the element is between l and r (inclusive)
        if element < l or element > r:
            return False
    
    # If all elements meet the requirements, return True
    return True

if __name__ == '__main__':
    a, l, r = map(int, input().split())
    print(get_number_of_partitions(a, l, r) % 998244353)


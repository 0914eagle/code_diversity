
def get_partitions(a, l, r):
    # Initialize a list to store the partitions
    partitions = []
    
    # Base case: if a is a single digit, return it as a list
    if a < 10:
        return [str(a)]
    
    # Recursive case: divide a into two parts
    for i in range(1, int(a ** 0.5) + 1):
        # Check if a is divisible by i
        if a % i == 0:
            # Get the two parts of a
            p1 = a // i
            p2 = a - p1
            
            # Recursively get the partitions of p1 and p2
            partitions1 = get_partitions(p1, l, r)
            partitions2 = get_partitions(p2, l, r)
            
            # Add the partitions of p1 and p2 to the list
            partitions.extend(partitions1)
            partitions.extend(partitions2)
    
    # Return the list of partitions
    return partitions

def count_beautiful_partitions(partitions, l, r):
    # Initialize a counter to store the number of beautiful partitions
    count = 0
    
    # Iterate through the partitions
    for partition in partitions:
        # Check if each element of the partition is between l and r (inclusive)
        if all(l <= int(i) <= r for i in partition):
            # Check if each element of the partition has no leading zeros
            if all(i[0] != '0' for i in partition):
                # Increment the counter
                count += 1
    
    # Return the counter
    return count

def main():
    # Read the input
    a, l, r = map(int, input().split())
    
    # Get the partitions of a
    partitions = get_partitions(a, l, r)
    
    # Count the beautiful partitions
    count = count_beautiful_partitions(partitions, l, r)
    
    # Print the result
    print(count % 998244353)

if __name__ == '__main__':
    main()


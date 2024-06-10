
def get_partitions(a, l, r):
    # Initialize a list to store the partitions
    partitions = []
    
    # Base case: if a is 0, return an empty list
    if a == 0:
        return partitions
    
    # Recursive case: split a into two parts
    for i in range(1, a + 1):
        # Check if i is between l and r (inclusive)
        if l <= i <= r:
            # Recursively call the function for the left part
            left_partitions = get_partitions(a - i, l, r)
            
            # Add i to the list of partitions
            partitions += [[i] + p for p in left_partitions]
    
    return partitions

def count_beautiful_partitions(partitions):
    # Initialize a counter for beautiful partitions
    beautiful_partitions = 0
    
    # Iterate over the partitions
    for partition in partitions:
        # Check if each element in the partition contains no leading zeros
        if all(int(s) == s for s in partition):
            beautiful_partitions += 1
    
    return beautiful_partitions

def main():
    # Read the input
    a = int(input())
    l = int(input())
    r = int(input())
    
    # Get the partitions of a
    partitions = get_partitions(a, l, r)
    
    # Count the beautiful partitions
    beautiful_partitions = count_beautiful_partitions(partitions)
    
    # Print the result modulo 998244353
    print(beautiful_partitions % 998244353)

if __name__ == '__main__':
    main()


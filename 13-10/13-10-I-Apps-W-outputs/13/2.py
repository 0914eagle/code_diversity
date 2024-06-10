
def count_partitions(a, l, r):
    # Initialize a list to store the partitions
    partitions = []
    
    # Iterate over the digits of 'a'
    for i in range(len(str(a))):
        # Get the current digit
        digit = int(str(a)[i])
        
        # Check if the current digit is within the range 'l' to 'r'
        if l <= digit <= r:
            # If the current digit is valid, add it to the current partition
            partitions.append(digit)
        else:
            # If the current digit is not valid, start a new partition
            partitions.append([digit])
    
    # Return the number of valid partitions
    return len(partitions)

def main():
    # Read the input
    a = int(input())
    l = int(input())
    r = int(input())
    
    # Call the count_partitions function and print the result
    print(count_partitions(a, l, r) % 998244353)

if __name__ == '__main__':
    main()



def number_of_beautiful_partitions(a, l, r):
    # Initialize a list to store the partitions
    partitions = []
    
    # Iterate over the digits of 'a'
    for i in range(len(str(a))):
        # Get the current digit
        digit = str(a)[i]
        
        # If the current digit is not zero, add it to the current partition
        if digit != "0":
            partitions.append(digit)
        
        # If the current digit is zero and the current partition is not empty, add it to the list of partitions
        elif partitions:
            partitions.append(digit)
    
    # Initialize a variable to store the number of beautiful partitions
    beautiful_partitions = 0
    
    # Iterate over the partitions
    for partition in partitions:
        # If the current partition is between 'l' and 'r' (inclusive), add it to the number of beautiful partitions
        if int(partition) >= l and int(partition) <= r:
            beautiful_partitions += 1
    
    # Return the number of beautiful partitions modulo 998244353
    return beautiful_partitions % 998244353

def main():
    # Read the input
    a = int(input())
    l = int(input())
    r = int(input())
    
    # Call the number_of_beautiful_partitions function
    result = number_of_beautiful_partitions(a, l, r)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()


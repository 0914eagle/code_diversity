
def get_xor_pairs(numbers):
    # Initialize a dictionary to store the count of xor pairs for each number
    xor_pairs = {}
    for i in range(len(numbers)):
        xor_pairs[i] = 0
    
    # Iterate through the numbers and calculate the xor pair count for each number
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            xor = numbers[i] ^ numbers[j]
            if xor in xor_pairs:
                xor_pairs[i] += 1
                xor_pairs[j] += 1
    
    # Return the sum of xor pairs
    return sum(xor_pairs.values())

def main():
    # Read the input data
    N = int(input())
    numbers = list(map(int, input().split()))
    
    # Calculate the xor pairs
    xor_pairs = get_xor_pairs(numbers)
    
    # Print the result
    print(xor_pairs)

if __name__ == '__main__':
    main()


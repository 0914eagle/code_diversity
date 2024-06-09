
def count_blocks(n):
    # Initialize a list to store the counts of blocks of length i
    counts = [0] * (n + 1)
    
    # Iterate over all integers from 0 to 10^n - 1
    for i in range(10**n):
        # Convert the integer to a string
        s = str(i)
        
        # Initialize a variable to store the length of the current block
        block_len = 1
        
        # Iterate over the characters in the string, starting from the second character
        for j in range(1, len(s)):
            # If the current character is the same as the previous character, increment the block length
            if s[j] == s[j-1]:
                block_len += 1
            # Otherwise, update the count for the current block length and reset the block length to 1
            else:
                counts[block_len] += 1
                block_len = 1
        
        # Update the count for the last block length
        counts[block_len] += 1
    
    return [count % 998244353 for count in counts]

if __name__ == '__main__':
    n = int(input())
    print(*count_blocks(n), sep='\n')


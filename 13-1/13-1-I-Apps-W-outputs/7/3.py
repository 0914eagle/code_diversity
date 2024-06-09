
def count_blocks(n):
    # Initialize a list to store the number of blocks of each length
    blocks = [0] * (n + 1)
    
    # Iterate through all integers from 0 to 10^n - 1
    for i in range(10**n):
        # Convert the integer to a string
        str_i = str(i)
        
        # Initialize a variable to store the length of the current block
        block_len = 1
        
        # Iterate through the characters of the string, starting from the second character
        for j in range(1, len(str_i)):
            # If the current character is the same as the previous character, increment the block length
            if str_i[j] == str_i[j-1]:
                block_len += 1
            # Otherwise, reset the block length to 1
            else:
                block_len = 1
            
            # Update the number of blocks of length block_len
            blocks[block_len] += 1
    
    # Return the number of blocks of each length, modulo 998244353
    return [x % 998244353 for x in blocks]

if __name__ == '__main__':
    n = int(input())
    print(*count_blocks(n), sep='\n')


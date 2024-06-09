
def count_regular_bracket_sequences(n, s):
    # Initialize the number of regular bracket sequences to 0
    count = 0
    
    # Loop through all possible bracket sequences of length 2n
    for i in range(2**(2*n)):
        # Convert the binary representation of i to a binary string of length 2n
        binary_string = bin(i)[2:].zfill(2*n)
        
        # Check if the binary string contains the given bracket sequence s as a substring
        if s in binary_string:
            # Check if the binary string is a regular bracket sequence
            if is_regular_bracket_sequence(binary_string):
                # Increment the number of regular bracket sequences
                count += 1
    
    # Return the number of regular bracket sequences modulo 1000000007
    return count % 1000000007

def is_regular_bracket_sequence(s):
    # Initialize a stack to keep track of the opening and closing brackets
    stack = []
    
    # Loop through the characters of the string s
    for c in s:
        # If the character is an opening bracket, push it to the stack
        if c == '(':
            stack.append(c)
        # If the character is a closing bracket, pop the top element from the stack if it is an opening bracket
        elif c == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
            else:
                stack.pop()
    
    # If the stack is empty, the string is a regular bracket sequence
    return len(stack) == 0

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(count_regular_bracket_sequences(n, s))


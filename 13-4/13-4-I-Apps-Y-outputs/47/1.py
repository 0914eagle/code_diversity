
def f1(n, s):
    # Initialize the result
    result = 0
    
    # Iterate over all possible positions of s in the regular bracket sequence
    for i in range(len(s)):
        # Check if s is a substring of the regular bracket sequence
        if s in generate_bracket_sequence(n, i):
            # Increment the result
            result += 1
    
    # Return the result modulo 10^9 + 7
    return result % 1000000007

def generate_bracket_sequence(n, i):
    # Initialize the result
    result = ""
    
    # Generate the regular bracket sequence
    for j in range(n):
        # Add the opening bracket
        result += "("
        # Add the closing bracket
        result += ")"
    
    # Add the substring
    result = result[:i] + s + result[i:]
    
    # Return the result
    return result

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(f1(n, s))


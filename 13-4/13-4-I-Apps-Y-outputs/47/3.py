
def f1(n, s):
    # Initialize the number of regular bracket sequences to 0
    num_seqs = 0
    
    # Loop through all possible combinations of '(' and ')' with length 2n
    for comb in itertools.product('()', repeat=2*n):
        # Initialize a variable to store the current combination
        current_comb = ''
        
        # Loop through each character in the current combination
        for char in comb:
            # If the current character is '(' or ')', add it to the current combination
            if char in '()':
                current_comb += char
            # If the current character is '1', add it to the current combination if the previous character is '(' and the next character is ')'
            elif char == '1' and comb[comb.index(char)-1] == '(' and comb[comb.index(char)+1] == ')':
                current_comb += char
        
        # If the current combination contains the given bracket sequence as a substring, increment the number of regular bracket sequences
        if s in current_comb:
            num_seqs += 1
    
    # Return the number of regular bracket sequences modulo 1000000007
    return num_seqs % 1000000007

def f2(n, s):
    # Initialize the number of regular bracket sequences to 0
    num_seqs = 0
    
    # Loop through all possible combinations of '(' and ')' with length 2n
    for comb in itertools.product('()', repeat=2*n):
        # Initialize a variable to store the current combination
        current_comb = ''
        
        # Loop through each character in the current combination
        for char in comb:
            # If the current character is '(' or ')', add it to the current combination
            if char in '()':
                current_comb += char
            # If the current character is '1', add it to the current combination if the previous character is '(' and the next character is ')'
            elif char == '1' and comb[comb.index(char)-1] == '(' and comb[comb.index(char)+1] == ')':
                current_comb += char
        
        # If the current combination contains the given bracket sequence as a substring, increment the number of regular bracket sequences
        if s in current_comb:
            num_seqs += 1
    
    # Return the number of regular bracket sequences modulo 1000000007
    return num_seqs % 1000000007

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(f1(n, s))


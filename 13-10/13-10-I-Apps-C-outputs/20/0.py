
def get_answer(a, b):
    # Initialize a set to store the appearances of numbers
    appearances = set()
    
    # Iterate through the rows of the table
    for i in range(1, b + 1):
        # Get the value of the current cell
        value = i
        
        # If the current cell is not in the first column, add the value of the cell to the left of it
        if i > a:
            value += get_reverse(value)
        
        # Add the value to the set of appearances
        appearances.add(value)
    
    # Return the length of the set of appearances
    return len(appearances)

def get_reverse(n):
    # Initialize an empty string to store the reverse of the number
    rev = ""
    
    # Iterate through the digits of the number
    while n > 0:
        # Get the last digit of the number
        digit = n % 10
        
        # Add the digit to the beginning of the string
        rev = str(digit) + rev
        
        # Remove the last digit of the number
        n //= 10
    
    # Return the reverse of the number
    return int(rev)

if __name__ == '__main__':
    q = int(input())
    
    for i in range(q):
        a, b = map(int, input().split())
        print(get_answer(a, b))



def get_max_value(expression, num_plus, num_minus):
    # Convert the expression to a list of tokens
    tokens = expression.split()
    
    # Initialize the maximum value
    max_value = 0
    
    # Iterate over the tokens
    for i in range(len(tokens)):
        # Check if the current token is a number
        if tokens[i].isdigit():
            # Convert the token to an integer
            num = int(tokens[i])
            
            # Check if the previous token is a plus or minus sign
            if i > 0 and tokens[i-1] in ["+", "-"]:
                # Get the previous token
                prev_token = tokens[i-1]
                
                # Check if the previous token is a plus sign
                if prev_token == "+":
                    # Add the number to the maximum value
                    max_value += num
                else:
                    # Subtract the number from the maximum value
                    max_value -= num
            else:
                # Add the number to the maximum value
                max_value += num
    
    # Return the maximum value
    return max_value

def main():
    # Read the expression from stdin
    expression = input()
    
    # Read the number of plus and minus operators from stdin
    num_plus, num_minus = map(int, input().split())
    
    # Call the get_max_value function
    max_value = get_max_value(expression, num_plus, num_minus)
    
    # Print the maximum value
    print(max_value)

if __name__ == '__main__':
    main()


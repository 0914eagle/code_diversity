
def get_shortest_correct_sequence(S):
    # Initialize the result string
    result = ""

    # Iterate through the input string
    for char in S:
        # If the current character is a left parenthesis, append it to the result
        if char == "(":
            result += "("
        # If the current character is a right parenthesis, append it to the result
        elif char == ")":
            result += ")"
        # If the current character is a left parenthesis, append it to the result
        elif char == ")":
            result += ")"

    # Return the result
    return result

def main():
    # Read the input from stdin
    N = int(input())
    S = input()

    # Call the function to get the shortest correct sequence
    result = get_shortest_correct_sequence(S)

    # Print the result
    print(result)

if __name__ == '__main__':
    main()


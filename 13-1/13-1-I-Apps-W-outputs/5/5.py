
def get_shortest_correct_bracket_sequence(S):
    # Initialize the result string
    result = ""

    # Iterate through the input string
    for char in S:
        # If the current character is a closing bracket, append it to the result
        if char == ")":
            result += ")"
        # If the current character is an opening bracket, append it to the result and check if the previous character was a closing bracket
        elif char == "(":
            result += "("
            if len(result) > 1 and result[-2] == ")":
                result = result[:-1] + "(" + result[-1]

    # Return the result
    return result

def main():
    # Read the input string
    S = input()

    # Get the shortest correct bracket sequence
    result = get_shortest_correct_bracket_sequence(S)

    # Print the result
    print(result)

if __name__ == '__main__':
    main()


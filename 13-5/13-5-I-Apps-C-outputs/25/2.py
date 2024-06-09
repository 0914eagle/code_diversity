
def get_keypress_solution(word):
    # Initialize the solution with the first keypress, which is the first letter of the word
    solution = word[0]
    
    # Iterate through the remaining letters of the word
    for i in range(1, len(word)):
        # If the current letter is the same as the previous letter, press the "right" key
        if word[i] == word[i-1]:
            solution += "R"
        # Otherwise, press the "up" key the appropriate number of times to reach the current letter
        else:
            solution += "U" + str(ord(word[i]) - ord(word[i-1]) + 1)
    
    return solution

def main():
    # Read the number of words to type
    q = int(input())
    
    # Iterate through each word
    for _ in range(q):
        # Read the word
        word = input()
        
        # Get the keypress solution for the word
        solution = get_keypress_solution(word)
        
        # Print the solution
        print(solution)

if __name__ == '__main__':
    main()


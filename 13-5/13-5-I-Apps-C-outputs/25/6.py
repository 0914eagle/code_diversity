
def get_keypress_solution(dictionary, word):
    # Initialize variables
    keypress_solution = []
    current_word = ""
    current_index = 0

    # Loop through each character in the word
    for char in word:
        # If the current character is not in the dictionary, break the loop
        if char not in dictionary:
            break
        # If the current character is in the dictionary, add it to the current word
        current_word += char
        # If the current word is in the dictionary, add the keypress solution for that word to the keypress solution for the current word
        if current_word in dictionary:
            keypress_solution += get_keypress_solution_for_word(current_word)
            # Reset the current word and index
            current_word = ""
            current_index = 0
        # If the current word is not in the dictionary, add the keypress solution for the current character to the keypress solution for the current word
        else:
            keypress_solution += get_keypress_solution_for_character(char)
            # Increment the current index
            current_index += 1

    # If the current word is in the dictionary, add the keypress solution for the current word to the keypress solution
    if current_word in dictionary:
        keypress_solution += get_keypress_solution_for_word(current_word)

    return keypress_solution

def get_keypress_solution_for_word(word):
    # Initialize variables
    keypress_solution = []
    current_index = 0

    # Loop through each character in the word
    for char in word:
        # If the current character is not in the dictionary, break the loop
        if char not in dictionary:
            break
        # If the current character is in the dictionary, add the keypress solution for the current character to the keypress solution
        keypress_solution += get_keypress_solution_for_character(char)
        # Increment the current index
        current_index += 1

    return keypress_solution

def get_keypress_solution_for_character(char):
    # Initialize variables
    keypress_solution = []

    # Loop through each digit in the dictionary
    for digit in dictionary:
        # If the current character is in the dictionary, add the keypress solution for the current digit to the keypress solution
        if char in dictionary[digit]:
            keypress_solution.append(digit)
            break

    return keypress_solution

def main():
    # Read the input
    dictionary_size, *dictionary = input().split()
    query_count = int(input())
    queries = [input() for _ in range(query_count)]

    # Initialize the output
    output = []

    # Loop through each query
    for query in queries:
        # Get the keypress solution for the query
        keypress_solution = get_keypress_solution(dictionary, query)
        # Add the keypress solution to the output
        output.append("".join(str(x) for x in keypress_solution))

    # Print the output
    print("\n".join(output))

if __name__ == '__main__':
    main()


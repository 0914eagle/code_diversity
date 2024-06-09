
def get_keypress_solution(word, dictionary):
    
    # Initialize the solution as an empty string
    solution = ""
    
    # Iterate through the word
    for i in range(len(word)):
        # Get the current character and the next character
        char = word[i]
        next_char = word[i+1] if i < len(word)-1 else ""
        
        # If the current character is not in the dictionary, break the word into parts
        if char not in dictionary:
            # Add the current character to the solution
            solution += str(char)
            # Add the "right" keypress to the solution
            solution += "R"
            # Break the word into parts
            for part in break_word(word[i:], dictionary):
                # Add the part to the solution
                solution += part
                # Add the "right" keypress to the solution
                solution += "R"
            # Break out of the loop
            break
        # If the current character is in the dictionary, check if the next character is also in the dictionary
        elif next_char in dictionary:
            # Add the current character to the solution
            solution += str(char)
        # If the next character is not in the dictionary, break the word into parts
        else:
            # Add the current character to the solution
            solution += str(char)
            # Add the "right" keypress to the solution
            solution += "R"
            # Break the word into parts
            for part in break_word(word[i+1:], dictionary):
                # Add the part to the solution
                solution += part
                # Add the "right" keypress to the solution
                solution += "R"
            # Break out of the loop
            break
    
    # Return the solution
    return solution

def break_word(word, dictionary):
    
    # Initialize the parts list
    parts = []
    
    # Iterate through the word
    for i in range(len(word)):
        # Get the current character and the next character
        char = word[i]
        next_char = word[i+1] if i < len(word)-1 else ""
        
        # If the current character is not in the dictionary, break the word into parts
        if char not in dictionary:
            # Add the current character to the parts list
            parts.append(str(char))
            # Break the word into parts
            for part in break_word(word[i:], dictionary):
                # Add the part to the parts list
                parts.append(part)
            # Break out of the loop
            break
        # If the current character is in the dictionary, check if the next character is also in the dictionary
        elif next_char in dictionary:
            # Add the current character to the parts list
            parts.append(str(char))
        # If the next character is not in the dictionary, break the word into parts
        else:
            # Add the current character to the parts list
            parts.append(str(char))
            # Break the word into parts
            for part in break_word(word[i+1:], dictionary):
                # Add the part to the parts list
                parts.append(part)
            # Break out of the loop
            break
    
    # Return the parts list
    return parts

def main():
    # Read the input
    dictionary_size, *dictionary = input().split()
    query_count = int(input())
    queries = [input() for _ in range(query_count)]
    
    # Iterate through the queries
    for query in queries:
        # Get the optimal keypress solution for the query
        solution = get_keypress_solution(query, dictionary)
        # Print the solution
        print(solution)

if __name__ == '__main__':
    main()


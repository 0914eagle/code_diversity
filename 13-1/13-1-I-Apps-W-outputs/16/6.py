
def minify_js(reserved_tokens, source_code):
    # Initialize the target word list
    target_word_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    target_word_list += [word + word[1:] for word in target_word_list]
    
    # Initialize the minified source code
    minified_source_code = ""
    
    # Iterate through each line of the source code
    for line in source_code.splitlines():
        # Initialize the current line of the minified source code
        minified_line = ""
        
        # Iterate through each token in the line
        for token in line.split():
            # Check if the token is a reserved token
            if token in reserved_tokens:
                # Add the reserved token to the minified line
                minified_line += token + " "
            # Check if the token is a number
            elif token.isdigit():
                # Add the number to the minified line
                minified_line += token + " "
            # Check if the token is a word
            elif token.isalpha():
                # Check if the word is in the target word list
                if token in target_word_list:
                    # Replace the word with the corresponding target word
                    minified_line += target_word_list[target_word_list.index(token)] + " "
                # Otherwise, add the word to the minified line
                else:
                    minified_line += token + " "
        
        # Add the minified line to the minified source code
        minified_source_code += minified_line.strip() + "\n"
    
    # Return the minified source code
    return minified_source_code.strip()



def solve(text):
    # Initialize an empty string to store the corrected text
    corrected_text = ""
    
    # Iterate through the input text
    for char in text:
        # If the current character is not '<', add it to the corrected text
        if char != "<":
            corrected_text += char
        # If the current character is '<' and the previous character is not '<', remove the previous character from the corrected text
        elif corrected_text and corrected_text[-1] != "<":
            corrected_text = corrected_text[:-1]
    
    # Return the corrected text
    return corrected_text


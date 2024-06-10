
def is_easily_playable(s):
    # Initialize variables to keep track of the positions
    odd_positions = []
    even_positions = []
    
    # Iterate through the string and append the characters to the appropriate list
    for i, char in enumerate(s):
        if i % 2 == 0:
            even_positions.append(char)
        else:
            odd_positions.append(char)
    
    # Check if all the characters in odd positions are R, U, or D
    for char in odd_positions:
        if char not in "RUD":
            return "No"
    
    # Check if all the characters in even positions are L, U, or D
    for char in even_positions:
        if char not in "LUD":
            return "No"
    
    # If all the conditions are met, return "Yes"
    return "Yes"

def main():
    s = input()
    print(is_easily_playable(s))

if __name__ == '__main__':
    main()



def get_name_for_number(k):
    # Initialize a list to store the possible names
    names = []
    
    # Iterate through all lowercase letters
    for letter in string.ascii_lowercase:
        # Calculate the absolute value of the difference between the current letter and the target number
        diff = abs(ord(letter) - k)
        
        # If the difference is zero, add the current letter to the list of possible names
        if diff == 0:
            names.append(letter)
        
        # If the difference is greater than zero, check if the current letter is within the range of possible names
        elif diff <= 26:
            # If the current letter is within the range, add it to the list of possible names
            names.append(letter)
    
    # Return the shortest name in the list of possible names
    return min(names, key=len)

def main():
    # Read a single line of input from stdin and convert it to an integer
    k = int(input().strip())
    
    # Print the name that the ninja should put on his nametag
    print(get_name_for_number(k))

if __name__ == '__main__':
    main()


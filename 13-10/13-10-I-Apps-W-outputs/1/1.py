
def get_encoded_number(k):
    # Initialize a list to store the encoded number
    encoded_number = []
    
    # Iterate through the alphabet
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        # Calculate the absolute difference between the current letter and the target number
        absolute_difference = abs(ord(letter) - k)
        
        # Add the absolute difference to the encoded number
        encoded_number.append(absolute_difference)
    
    # Return the encoded number
    return encoded_number

def get_shortest_name(k):
    # Initialize a list to store the possible names
    names = []
    
    # Iterate through the alphabet
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        # Calculate the encoded number for the current letter
        encoded_number = get_encoded_number(k)
        
        # Check if the encoded number is equal to the target number
        if encoded_number == k:
            # Add the current letter to the list of possible names
            names.append(letter)
    
    # Return the shortest name
    return min(names, key=len)

def main():
    # Take input from the user
    k = int(input())
    
    # Calculate the shortest name
    shortest_name = get_shortest_name(k)
    
    # Print the shortest name
    print(shortest_name)

if __name__ == '__main__':
    main()


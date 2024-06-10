
def encode_number(k):
    # Initialize an empty string to store the encoded name
    encoded_name = ""
    
    # Iterate through the alphabet (lowercase letters)
    for letter in "abcdefghijklmnopqrstuvwxyz":
        # Calculate the absolute difference between the letter's position in the alphabet and the input number
        diff = abs(ord(letter) - k)
        
        # If the difference is less than or equal to the current encoded name, update the encoded name
        if diff <= len(encoded_name):
            encoded_name = letter
    
    return encoded_name

def decode_name(name):
    # Initialize the decoded number to 0
    decoded_number = 0
    
    # Iterate through the name
    for letter in name:
        # Calculate the difference between the letter's position in the alphabet and the current decoded number
        diff = abs(ord(letter) - decoded_number)
        
        # Update the decoded number by adding the difference
        decoded_number += diff
    
    return decoded_number

def find_shortest_name(k):
    # Initialize an empty string to store the shortest name
    shortest_name = ""
    
    # Iterate through the alphabet (lowercase letters)
    for letter in "abcdefghijklmnopqrstuvwxyz":
        # Encode the number using the current letter
        encoded_name = letter * k
        
        # If the encoded name is shorter than the current shortest name, update the shortest name
        if len(encoded_name) < len(shortest_name) or shortest_name == "":
            shortest_name = encoded_name
    
    return shortest_name

def main():
    # Take input from the user
    k = int(input())
    
    # Find the shortest name that encodes to the input number
    shortest_name = find_shortest_name(k)
    
    # Print the shortest name
    print(shortest_name)

if __name__ == '__main__':
    main()


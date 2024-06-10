
def encode_number(k):
    # Initialize variables
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    name = ''
    count = 0
    
    # Loop through the alphabet until the encoded number is equal to the given number
    while count != k:
        for letter in alphabet:
            count += abs(alphabet.index(letter) - alphabet.index(name[-1]))
            if count == k:
                name += letter
                break
    
    # Return the encoded name
    return name

def main():
    # Read the input
    k = int(input())
    
    # Print the output
    print(encode_number(k))
    
if __name__ == '__main__':
    main()


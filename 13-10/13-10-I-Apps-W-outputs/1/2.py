
def get_nametag(k):
    # Initialize a dictionary to map each letter to its position in the alphabet
    letter_map = {}
    for i, letter in enumerate(string.ascii_lowercase):
        letter_map[letter] = i
    
    # Initialize a list to store the letters of the nametag
    nametag = []
    
    # Convert the input number to a list of letters
    while k > 0:
        k -= 1
        nametag.append(chr(97 + k % 26))
        k //= 26
    
    # Reverse the list to get the nametag in the correct order
    nametag.reverse()
    
    # Calculate the value of the nametag
    value = 0
    for i in range(len(nametag) - 1):
        value += abs(letter_map[nametag[i]] - letter_map[nametag[i + 1]])
    
    return "".join(nametag)

def main():
    k = int(input())
    print(get_nametag(k))

if __name__ == '__main__':
    main()


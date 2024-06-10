
def get_median(s, t, k):
    # Initialize an empty list to store the strings
    strings = []
    
    # Iterate over the lowercase Latin letters
    for letter in range(97, 97 + 26):
        # Check if the letter is between s and t
        if s <= chr(letter) <= t:
            # Add the letter to the list of strings
            strings.append(chr(letter))
    
    # Return the median of the list of strings
    return strings[len(strings) // 2]

def main():
    # Read the input k
    k = int(input())
    
    # Read the input s and t
    s = input()
    t = input()
    
    # Print the median
    print(get_median(s, t, k))

if __name__ == '__main__':
    main()


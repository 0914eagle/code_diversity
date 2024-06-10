
def get_key(words, array):
    # Initialize the key as a list of all 26 lowercase letters
    key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Create a dictionary to map each word to its index in the array
    word_to_index = {word: i for i, word in enumerate(array, 1)}
    
    # Iterate through each word in the array
    for i, word in enumerate(array, 1):
        # Find the index of the word in the words list
        index = words.index(word)
        
        # Swap the letter at index i with the letter at index word_to_index[word] in the key
        key[i], key[word_to_index[word]] = key[word_to_index[word]], key[i]
    
    # Return the key
    return ''.join(key)

def main():
    # Read the input from stdin
    N = int(input())
    words = []
    for _ in range(N):
        words.append(input())
    array = list(map(int, input().split()))
    
    # Call the get_key function and print the output
    key = get_key(words, array)
    if key == "NE":
        print("NE")
    else:
        print("DA")
        print(key)

if __name__ == '__main__':
    main()


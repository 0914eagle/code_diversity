
def get_key(words, array_a):
    
    # Initialize the key with the first word of the array
    key = words[array_a[0]]
    
    # Iterate through the remaining words in the array
    for i in range(1, len(array_a)):
        # Get the word currently located at position i in the array
        word = words[array_a[i]]
        
        # Check if the word is already in the key
        if word in key:
            # If it is, continue to the next word
            continue
        
        # Check if the word can be inserted into the key without violating the lexicographic order
        if can_insert_word(key, word):
            # If it can, insert it into the key
            key += word
        else:
            # If it can't, return "NE"
            return "NE"
    
    # If we made it this far, return the key
    return key

def can_insert_word(key, word):
    
    # Check if the word is a prefix of the key
    if word in key:
        return False
    
    # Check if the word is lexicographically larger than the last letter of the key
    if word < key[-1]:
        return False
    
    # Check if the word is lexicographically smaller than the first letter of the key
    if word > key[0]:
        return False
    
    # If we made it this far, return True
    return True

def main():
    # Read the input
    num_words = int(input())
    words = []
    for _ in range(num_words):
        words.append(input())
    array_a = list(map(int, input().split()))
    
    # Get the key
    key = get_key(words, array_a)
    
    # Print the output
    if key == "NE":
        print("NE")
    else:
        print("DA")
        print(key)

if __name__ == '__main__':
    main()


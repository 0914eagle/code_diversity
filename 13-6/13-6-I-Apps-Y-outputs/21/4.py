
def is_shiritori(words):
    # Initialize a set to store the words announced
    announced_words = set()
    
    # Iterate through the words
    for i in range(len(words)):
        # Check if the word has been announced before
        if words[i] in announced_words:
            return False
        # Add the word to the set of announced words
        announced_words.add(words[i])
    
    return True

def main():
    # Read the number of words from stdin
    num_words = int(input())
    
    # Read the words from stdin
    words = []
    for i in range(num_words):
        words.append(input())
    
    # Check if the rules of shiritori were observed
    if is_shiritori(words):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()


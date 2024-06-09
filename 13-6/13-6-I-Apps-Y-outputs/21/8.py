
def is_shiritori_observed(words):
    # Initialize a set to store the announced words
    announced_words = set()
    
    # Iterate through the list of words
    for word in words:
        # Check if the word has already been announced
        if word in announced_words:
            return False
        # Add the word to the set of announced words
        announced_words.add(word)
    
    return True

def main():
    # Read the number of words and the words from stdin
    num_words = int(input())
    words = [input() for _ in range(num_words)]
    
    # Check if the rules of shiritori were observed
    if is_shiritori_observed(words):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()


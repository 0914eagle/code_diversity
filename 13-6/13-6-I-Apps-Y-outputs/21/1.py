
def is_shiritori_observed(words):
    # Initialize a set to store the words announced
    announced_words = set()
    # Iterate through the words
    for word in words:
        # If the word has already been announced, return False
        if word in announced_words:
            return False
        # Add the word to the set of announced words
        announced_words.add(word)
    # If all words have been announced and no word has been repeated, return True
    return True

def main():
    # Read the number of words from stdin
    num_words = int(input())
    # Read the words from stdin
    words = [input() for _ in range(num_words)]
    # Check if the rules of shiritori were observed
    if is_shiritori_observed(words):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()


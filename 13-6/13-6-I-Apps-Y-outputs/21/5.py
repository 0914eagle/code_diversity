
def is_shiritori_observed(words):
    # Initialize a set to store the announced words
    announced_words = set()
    # Iterate through the words
    for word in words:
        # If the word is already in the set, return False
        if word in announced_words:
            return False
        # Add the word to the set
        announced_words.add(word)
    # If all words are unique, return True
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


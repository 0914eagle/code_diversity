
def is_shiritori_observed(words):
    # Initialize a set to store the words announced
    announced_words = set()
    
    # Iterate through the words
    for i in range(len(words)):
        # Check if the current word is already in the set of announced words
        if words[i] in announced_words:
            # If it is, return False
            return False
        # Add the current word to the set of announced words
        announced_words.add(words[i])
    
    # If all words are unique and satisfy the shiritori condition, return True
    return True

def main():
    # Read the number of words and the words from stdin
    num_words = int(input())
    words = []
    for i in range(num_words):
        words.append(input())
    
    # Check if the rules of shiritori were observed
    if is_shiritori_observed(words):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()


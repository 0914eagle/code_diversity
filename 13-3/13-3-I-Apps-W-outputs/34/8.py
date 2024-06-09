
def is_codeforces_substring(word):
    # Initialize a set to store the indices of the letters in the word
    indices = set()
    # Loop through each letter in the word
    for i, letter in enumerate(word):
        # If the letter is not in the set, add it to the set and continue
        if letter not in indices:
            indices.add(i)
        # If the letter is already in the set, return False
        else:
            return False
    # If all letters are unique, return True
    return True

def main():
    word = input()
    if is_codeforces_substring(word):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()



def is_codeforces_substring(word):
    # Initialize a set to store the indices of the letters in the word
    indices = set()
    # Loop through each letter in the word
    for i, letter in enumerate(word):
        # If the letter is 'C', add the index of the letter to the set
        if letter == "C":
            indices.add(i)
    # If the set contains the indices of the first three letters of CODEFORCES, return True
    if indices >= {0, 1, 2}:
        return True
    # Otherwise, return False
    return False

def main():
    word = input()
    if is_codeforces_substring(word):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()


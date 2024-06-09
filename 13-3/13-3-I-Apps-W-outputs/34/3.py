
def check_substring(word):
    
    # Initialize a set to store the indices of the letters in the word
    indices = set()
    # Loop through each letter in the word
    for i, letter in enumerate(word):
        # If the letter is not in the word CODEFORCES, add its index to the set
        if letter not in "CODEFORCES":
            indices.add(i)
    # If the set is empty, return True
    if not indices:
        return True
    # Initialize a variable to store the length of the word
    n = len(word)
    # Loop through each index in the set
    for i in indices:
        # If the index is 0 or n-1, return False
        if i in [0, n-1]:
            return False
        # If the index is not 0 or n-1, check if the substring starting from the index and ending at the next to last index forms the word CODEFORCES
        if word[i:n-1] == "CODEFORCES":
            return True
    # If none of the above conditions are met, return False
    return False

def main():
    word = input()
    if check_substring(word):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()


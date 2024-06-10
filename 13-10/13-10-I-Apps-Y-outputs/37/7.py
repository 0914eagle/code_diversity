
def get_smallest_missing_letter(s):
    # Initialize a set with all lowercase English letters
    letters = set("abcdefghijklmnopqrstuvwxyz")
    # Remove the letters in the input string from the set
    letters.difference_update(s)
    # If the set is empty, return "None"
    if not letters:
        return "None"
    # Return the smallest letter in the set
    return min(letters)

def main():
    s = input()
    print(get_smallest_missing_letter(s))

if __name__ == '__main__':
    main()


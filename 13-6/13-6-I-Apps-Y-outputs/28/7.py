
def check_counting(n, words):
    # Initialize a variable to store the current count
    count = 0
    # Iterate through the list of words
    for word in words:
        # If the word is a number, increment the count by the value of the word
        if word.isdigit():
            count += int(word)
        # If the word is "mumble", return "something is fishy"
        elif word == "mumble":
            return "something is fishy"
    # If the count is equal to the number of bites, return "makes sense"
    if count == n:
        return "makes sense"
    # Otherwise, return "something is fishy"
    else:
        return "something is fishy"



def solve(n, words):
    # Initialize a variable to keep track of Arild's count
    count = 0
    # Iterate through the list of words
    for word in words:
        # If the word is a number, increment Arild's count by that number
        if word.isdigit():
            count += int(word)
        # If the word is "mumble", decrement Arild's count by 1
        elif word == "mumble":
            count -= 1
    # If Arild's count is equal to the total number of bites, his counting makes sense
    if count == n:
        return "makes sense"
    # Otherwise, his counting is suspicious
    else:
        return "something is fishy"


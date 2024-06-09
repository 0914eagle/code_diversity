
def solve(n, words):
    # Initialize a variable to keep track of Arild's count
    count = 0
    
    # Iterate through the list of words
    for word in words:
        # If the word is a number, update the count
        if word.isdigit():
            count += int(word)
        # If the word is "mumble", something is fishy
        elif word == "mumble":
            return "something is fishy"
    
    # If the count is equal to the total number of bites, Arild's counting makes sense
    if count == n:
        return "makes sense"
    # Otherwise, something is fishy
    else:
        return "something is fishy"


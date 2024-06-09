
def find_photo(heights):
    # Initialize variables
    n = len(heights)
    you = 0
    alice = 0
    bob = 0

    # Find the indices of you, Alice, and Bob in the heights list
    for i in range(n):
        if heights[i] == 1:
            you = i
        elif heights[i] == 2:
            alice = i
        elif heights[i] == 3:
            bob = i

    # Check if Alice is to the left of you and Bob is to the right of you
    if alice < you and bob > you:
        return True
    else:
        return False


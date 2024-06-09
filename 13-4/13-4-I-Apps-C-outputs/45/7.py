
def solve(a):
    # Step 1: Find the minimal element in the sequence
    min_element = min(a)

    # Step 2: Count the number of elements that are divisible by the minimal element
    count = 0
    for element in a:
        if element % min_element == 0:
            count += 1

    # Step 3: Return the number of colors needed
    return count


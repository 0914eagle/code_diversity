
def solve(n, a, b, seats):
    # Initialize the result
    result = 0

    # Iterate over the seats
    for i in range(n):
        # Check if the current seat is empty
        if seats[i] == ".":
            # Check if the previous seat is empty and the next seat is empty
            if i > 0 and seats[i-1] == "." and (i == n-1 or seats[i+1] == "."):
                # Increment the result
                result += 1

    # Return the result
    return result



def solve(n, answers):
    # Initialize variables
    adrian_count = 0
    bruno_count = 0
    goran_count = 0

    # Iterate through the answers
    for i in range(n):
        # Check which answer is correct
        if answers[i] == "A":
            adrian_count += 1
            bruno_count += 1
            goran_count += 2
        elif answers[i] == "B":
            adrian_count += 2
            bruno_count += 1
            goran_count += 1
        else:
            adrian_count += 2
            bruno_count += 2
            goran_count += 1

    # Find the maximum number of correct answers
    max_count = max(adrian_count, bruno_count, goran_count)

    # Return the names of the boys with the maximum number of correct answers
    if adrian_count == max_count:
        return "Adrian"
    elif bruno_count == max_count:
        return "Bruno"
    else:
        return "Goran"


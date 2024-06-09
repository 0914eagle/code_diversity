
def solve(m, k, a, t, r):
    # Initialize a dictionary to store the number of portions of each dish
    dishes = {i: a[i-1] for i in range(1, k+1)}
    # Iterate through the observations of the passengers in front of Polycarp
    for i in range(m-1):
        # If the passenger was disappointed, it means they couldn't have their preferred dish
        if r[i] == 1:
            dishes[t[i]] -= 1
    # Initialize a string to store the answer
    answer = ""
    # Iterate through the dishes
    for i in range(1, k+1):
        # If the number of portions of the current dish is 0, it means it has run out
        if dishes[i] == 0:
            answer += "Y"
        # Otherwise, it is definitely available
        else:
            answer += "N"
    return answer


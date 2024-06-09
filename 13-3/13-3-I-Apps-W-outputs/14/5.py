
def solve(m, k, a, t, r):
    # Initialize a dictionary to keep track of the available dishes
    available_dishes = {i: True for i in range(1, k+1)}

    # Iterate over the observations of the passengers in front of Polycarp
    for i in range(m-1):
        # If the passenger was disappointed, it means they couldn't have the dish they wanted
        if r[i] == 1:
            available_dishes[t[i]] = False

    # Initialize the result string
    result = ""

    # Iterate over the dishes and check if they are available
    for i in range(1, k+1):
        if available_dishes[i]:
            result += "Y"
        else:
            result += "N"

    return result


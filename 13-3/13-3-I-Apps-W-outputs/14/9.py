
def solve(m, k, a, t, r):
    # Initialize a dictionary to keep track of the available dishes
    available_dishes = {i: a[i] for i in range(k)}

    # Iterate through the observations of the passengers in front of Polycarp
    for i in range(m - 1):
        # If the passenger was disappointed, it means they didn't get the dish they wanted
        if r[i] == 1:
            available_dishes[t[i]] -= 1

    # Initialize the answer as a string of "N"s
    answer = "N" * k

    # Iterate through the available dishes and check if they could have run out by the time Polycarp was served
    for i in range(k):
        if available_dishes[i] == 0:
            answer = answer[:i] + "Y" + answer[i + 1:]

    return answer


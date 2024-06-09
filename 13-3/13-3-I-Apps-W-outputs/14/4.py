
def solve(m, k, a, t, r):
    # Initialize a dictionary to keep track of the number of portions of each dish
    dishes = {i: a[i-1] for i in range(1, k+1)}
    # Iterate through the observations of the passengers in front of Polycarp
    for i in range(m-1):
        # If the passenger was disappointed, it means they didn't get the dish they wanted
        if r[i] == 1:
            dishes[t[i]] -= 1
    # Initialize a string to store the answer
    answer = ""
    # Iterate through the dishes and check if they could have run out by the time the stewardess reached Polycarp
    for i in range(1, k+1):
        if dishes[i] == 0:
            answer += "Y"
        else:
            answer += "N"
    return answer


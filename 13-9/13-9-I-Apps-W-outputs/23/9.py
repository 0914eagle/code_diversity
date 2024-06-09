
def solve(n, x1, x2, c):
    # Sort the servers in non-decreasing order of their specifications
    c_sorted = sorted(c)

    # Initialize the variables to keep track of the servers used for each service
    k1, k2 = 0, 0
    s1, s2 = [], []

    # Loop through the servers and assign them to either service 1 or service 2
    for i, ci in enumerate(c_sorted, 1):
        if x1 // i <= ci:
            k1 += 1
            s1.append(i)
        elif x2 // i <= ci:
            k2 += 1
            s2.append(i)
        else:
            break

    # Check if it is possible to deploy both services using the given servers
    if k1 == 0 or k2 == 0:
        return "No"

    # Return the results
    return "Yes\n" + str(k1) + " " + str(k2) + "\n" + " ".join(map(str, s1)) + "\n" + " ".join(map(str, s2))


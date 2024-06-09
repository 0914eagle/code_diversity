
def solve(n, a, b, c):
    # Sort the poll results by the measure a_i * S + b_i * T
    sorted_results = sorted(zip(a, b, c), key=lambda x: x[0] * S + x[1] * T)

    # Find the indices of the first and last results with c_i true
    j = 0
    k = 0
    for i in range(n):
        if sorted_results[i][2] == 1:
            j = i
            break
    for i in range(n-1, -1, -1):
        if sorted_results[i][2] == 1:
            k = i
            break

    # Return the smallest possible cluster size
    return k-j+1


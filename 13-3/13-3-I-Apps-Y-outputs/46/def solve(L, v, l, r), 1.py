
def solve(L, v, l, r):
    # Calculate the number of lanterns visible
    num_lanterns = 0
    for i in range(1, L+1):
        if i % v == 0 and i not in range(l, r+1):
            num_lanterns += 1
    return num_lanterns


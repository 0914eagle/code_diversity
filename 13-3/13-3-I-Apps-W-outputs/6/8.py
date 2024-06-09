
def solve(v, a):
    # Initialize a list to store the maximum number that can be written for each digit
    max_num = [0] * 10
    # Loop through the given numbers and find the maximum number that can be written for each digit
    for i in range(1, 10):
        if v >= a[i]:
            max_num[i] = 9 * a[i]
            v -= a[i]
        else:
            max_num[i] = v
            v = 0
    # If v is not enough to write any digit, return -1
    if v == 0:
        return -1
    # Initialize an empty string to store the maximum number
    max_str = ""
    # Loop through the maximum number for each digit and append it to the string
    for i in range(1, 10):
        max_str += str(max_num[i])
    return int(max_str)


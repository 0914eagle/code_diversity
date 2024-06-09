
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
    # If there is no enough paint for any digit, return -1
    if v > 0:
        return -1
    # Initialize an empty string to store the maximum number
    max_str = ""
    # Loop through the maximum numbers for each digit and concatenate them to the string
    for i in range(1, 10):
        if max_num[i] > 0:
            max_str += str(i) * int(max_num[i] / i)
    # Return the maximum number
    return max_str


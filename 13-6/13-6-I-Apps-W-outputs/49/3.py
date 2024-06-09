
def solve(n, arr):
    # Initialize the sequence with "+"
    seq = ["+"] * n
    # Loop through the array from the end to the beginning
    for i in range(n-1, -1, -1):
        # If the current element is greater than the previous element,
        # change the sign to "-"
        if arr[i] > arr[i+1]:
            seq[i] = "-"
    return "".join(seq)


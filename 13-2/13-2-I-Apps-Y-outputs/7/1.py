
def solve(s, t):
    # Initialize result string
    result = "UNRESTORABLE"

    # Iterate through all possible strings that satisfy Condition 1
    for i in range(26):
        curr_string = chr(ord('a') + i) + t + chr(ord('a') + i)
        if curr_string in s:
            # If the current string is lexicographically smallest, update result
            if curr_string < result:
                result = curr_string

    return result



def solve(s, k):
    # Initialize variables
    n = len(s)
    count = 0
    i = 0
    j = 0

    # Loop through the string
    while i < n and j < k:
        # If the current character is not 'R', 'G', or 'B', skip it
        if s[i] not in ["R", "G", "B"]:
            i += 1
            continue

        # If the current character is 'R', 'G', or 'B', check if it is part of the substring
        if s[i] == "R":
            if j == 0 or s[i - 1] in ["G", "B"]:
                j += 1
        elif s[i] == "G":
            if j == 0 or s[i - 1] in ["R", "B"]:
                j += 1
        elif s[i] == "B":
            if j == 0 or s[i - 1] in ["R", "G"]:
                j += 1

        # If we have found the substring, break the loop
        if j == k:
            break

        # Increment the count and move on to the next character
        count += 1
        i += 1

    # Return the count
    return count


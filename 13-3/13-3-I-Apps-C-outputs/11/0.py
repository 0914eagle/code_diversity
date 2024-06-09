
def solve(n, k, p, a, b):
    # Sort the positions of the people and keys
    a = sorted(a)
    b = sorted(b)
    
    # Initialize the time needed for each person to reach the office
    time_needed = [0] * n
    
    # Iterate through the people and keys
    for i in range(n):
        for j in range(k):
            # If the person is located before the key, they can take the key and go to the office
            if a[i] < b[j]:
                time_needed[i] += b[j] - a[i]
                break
    
    # Return the maximum time needed for all people to reach the office
    return max(time_needed)


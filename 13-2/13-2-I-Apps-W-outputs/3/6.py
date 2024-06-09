
def solve(password):
    n = len(password)
    if n == 1:
        return 1
    
    # Find the first two adjacent numbers that are not equal to each other
    for i in range(n-1):
        if password[i] != password[i+1]:
            break
    
    # If no such numbers exist, return the length of the password
    if i == n-1:
        return n
    
    # Replace the two numbers with their sum and return the length of the new password
    password[i] += password[i+1]
    del password[i+1]
    return solve(password)


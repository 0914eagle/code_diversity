
def solve(n, a, b, c):
    # Calculate the total number of cookies
    total_cookies = a + b + c
    
    # Initialize the maximum number of cookies that can be distributed
    max_cookies = 0
    
    # Loop through all possible combinations of cookies
    for i in range(total_cookies + 1):
        for j in range(total_cookies - i + 1):
            k = total_cookies - i - j
            
            # Check if the combination satisfies the conditions
            if i % n == 0 and j % n == 0 and k % n == 0:
                max_cookies = max(max_cookies, i + j + k)
    
    return max_cookies


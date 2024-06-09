
def solve(N, A, B, C):
    # Calculate the total number of cookies
    total_cookies = A + B + C
    
    # Initialize a list to store the number of cookies for each friend
    cookies_per_friend = [0] * (N + 1)
    
    # Loop through each friend and distribute the cookies
    for i in range(1, N + 1):
        # Calculate the number of cookies for this friend
        cookies_per_friend[i] = total_cookies // N
        
        # If there are any remaining cookies, distribute them equally among the first N friends
        if total_cookies % N != 0:
            for j in range(1, N + 1):
                cookies_per_friend[j] += 1
                total_cookies -= 1
    
    # Return the total number of cookies that can be distributed
    return sum(cookies_per_friend)


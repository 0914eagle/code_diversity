
def solve(N, A, B, C):
    # Calculate the total number of cookies
    total_cookies = A + B + C
    
    # Initialize a list to store the number of cookies for each friend
    cookies_per_friend = [0] * (N + 1)
    
    # Initialize variables to keep track of the current cookie type and the number of cookies left
    current_cookie_type = 1
    cookies_left = total_cookies
    
    # Loop through each friend and distribute the cookies
    for i in range(1, N + 1):
        # If there are no more cookies left, break the loop
        if cookies_left == 0:
            break
        
        # If the current cookie type is almond, switch to the next type
        if current_cookie_type == 1 and cookies_left >= A:
            current_cookie_type = 2
        # If the current cookie type is butter, switch to the next type
        elif current_cookie_type == 2 and cookies_left >= B:
            current_cookie_type = 3
        # If the current cookie type is chocolate, switch to the next type
        elif current_cookie_type == 3 and cookies_left >= C:
            current_cookie_type = 1
        
        # Determine the number of cookies to give the current friend
        if current_cookie_type == 1:
            cookies_per_friend[i] = min(A, cookies_left)
        elif current_cookie_type == 2:
            cookies_per_friend[i] = min(B, cookies_left)
        else:
            cookies_per_friend[i] = min(C, cookies_left)
        
        # Subtract the number of cookies given from the total number of cookies left
        cookies_left -= cookies_per_friend[i]
    
    # Return the total number of cookies distributed
    return sum(cookies_per_friend)


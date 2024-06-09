
def solve(N, A, B, C):
    # Calculate the total number of cookies
    total_cookies = A + B + C
    
    # Initialize a list to store the number of cookies for each friend
    cookies_per_friend = [0] * (N + 1)
    
    # Initialize variables to keep track of the current cookie type and the number of cookies left
    current_cookie_type = 1
    cookies_left = total_cookies
    
    # Loop through each friend and distribute the cookies
    for friend in range(1, N + 1):
        # If there are no more cookies left, break the loop
        if cookies_left == 0:
            break
        
        # If the current cookie type is almond, assign it to the current friend
        if current_cookie_type == 1:
            cookies_per_friend[friend] += 1
            cookies_left -= 1
        
        # If the current cookie type is butter, assign it to the current friend
        elif current_cookie_type == 2:
            cookies_per_friend[friend] += 1
            cookies_left -= 1
        
        # If the current cookie type is chocolate, assign it to the current friend
        elif current_cookie_type == 3:
            cookies_per_friend[friend] += 1
            cookies_left -= 1
        
        # Update the current cookie type
        current_cookie_type = (current_cookie_type % 3) + 1
    
    # Return the total number of cookies distributed
    return total_cookies - cookies_left


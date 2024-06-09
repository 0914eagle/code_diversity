
def solve(N, A, B, C):
    # Calculate the total number of cookies
    total_cookies = A + B + C
    
    # Initialize a list to store the number of cookies for each friend
    cookies_per_friend = [0] * (N + 1)
    
    # Initialize variables to keep track of the current cookie type and the number of cookies left
    current_cookie_type = 0
    num_cookies_left = total_cookies
    
    # Loop through each friend and assign them cookies
    for i in range(1, N + 1):
        # If there are no more cookies left, break the loop
        if num_cookies_left == 0:
            break
        
        # If the current cookie type is 0, assign the next cookie type
        if current_cookie_type == 0:
            current_cookie_type = 1
        # If the current cookie type is 1, assign the next cookie type
        elif current_cookie_type == 1:
            current_cookie_type = 2
        # If the current cookie type is 2, assign the next cookie type
        elif current_cookie_type == 2:
            current_cookie_type = 0
        
        # Assign the current cookie type to the current friend
        cookies_per_friend[i] = current_cookie_type
        
        # Decrement the number of cookies left
        num_cookies_left -= 1
    
    # Return the total number of cookies distributed
    return sum(cookies_per_friend)


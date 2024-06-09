
def solve(N, A, B, C):
    # Calculate the total number of cookies
    total_cookies = A + B + C
    
    # Initialize a list to store the number of cookies for each friend
    cookies_per_friend = [0] * (N + 1)
    
    # Initialize variables to keep track of the current cookie type and the number of cookies left
    current_cookie_type = 1
    num_cookies_left = total_cookies
    
    # Loop through each friend and assign them cookies
    for i in range(1, N + 1):
        # If there are no more cookies left, break the loop
        if num_cookies_left == 0:
            break
        
        # Assign the current cookie type to the current friend
        cookies_per_friend[i] = current_cookie_type
        
        # Decrement the number of cookies left
        num_cookies_left -= 1
        
        # If there are no more cookies of the current type left, move on to the next type
        if num_cookies_left == 0:
            current_cookie_type += 1
            num_cookies_left = total_cookies - (current_cookie_type - 1) * A - (current_cookie_type - 2) * B - (current_cookie_type - 3) * C
    
    # Return the total number of cookies distributed
    return sum(cookies_per_friend)


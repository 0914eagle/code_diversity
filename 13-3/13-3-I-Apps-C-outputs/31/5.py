
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
        
        # If the current cookie type is almond, distribute the almond cookies
        if current_cookie_type == 1:
            # If there are no almond cookies left, move on to the next cookie type
            if A == 0:
                current_cookie_type += 1
                continue
            # Otherwise, distribute an almond cookie to the current friend
            else:
                cookies_per_friend[i] += 1
                A -= 1
                cookies_left -= 1
        
        # If the current cookie type is butter, distribute the butter cookies
        elif current_cookie_type == 2:
            # If there are no butter cookies left, move on to the next cookie type
            if B == 0:
                current_cookie_type += 1
                continue
            # Otherwise, distribute a butter cookie to the current friend
            else:
                cookies_per_friend[i] += 1
                B -= 1
                cookies_left -= 1
        
        # If the current cookie type is chocolate, distribute the chocolate cookies
        elif current_cookie_type == 3:
            # If there are no chocolate cookies left, move on to the next cookie type
            if C == 0:
                current_cookie_type += 1
                continue
            # Otherwise, distribute a chocolate cookie to the current friend
            else:
                cookies_per_friend[i] += 1
                C -= 1
                cookies_left -= 1
    
    # Return the maximum number of cookies that can be distributed
    return max(cookies_per_friend)


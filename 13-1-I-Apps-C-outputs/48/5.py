
def max_cookies(job_offers):
    # Sort the job offers in ascending order
    job_offers.sort()
    # Initialize the maximum number of cookies to 0
    max_cookies = 0
    # Loop through the job offers
    for i in range(len(job_offers)):
        # Calculate the time between the current job offer and the previous job offer
        time_diff = job_offers[i] - job_offers[i-1] if i > 0 else 0
        # If the time difference is greater than or equal to 400000, accept the current job offer and calculate the number of cookies earned
        if time_diff >= 400000:
            # Calculate the number of cookies earned based on the length of the slide
            cookies = (job_offers[i] - job_offers[i-1]) // 100000 if i > 0 else job_offers[i] // 100000
            # Update the maximum number of cookies if the current number of cookies is greater
            max_cookies = max(max_cookies, cookies)
    # Return the maximum number of cookies
    return max_cookies


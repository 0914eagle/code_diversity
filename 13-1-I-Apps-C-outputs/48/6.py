
def max_cookies(job_offers):
    # Sort the job offers in ascending order
    job_offers.sort()
    # Initialize the maximum number of cookies to 0
    max_cookies = 0
    # Loop through the job offers
    for i in range(len(job_offers)):
        # Calculate the time between the current job offer and the previous job offer
        time_diff = job_offers[i] - job_offers[i-1] if i > 0 else 0
        # Check if the time difference is at least 400000 milliseconds
        if time_diff >= 400000:
            # Add the number of cookies for the current job offer to the maximum number of cookies
            max_cookies += 1
    return max_cookies


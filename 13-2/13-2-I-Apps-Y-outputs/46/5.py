
def worm_climbing(a, b, h):
    # Calculate the number of times the worm needs to crawl up
    num_crawls = h // a
    
    # Calculate the number of inches the worm falls during the resting period
    fall_inches = b * (num_crawls - 1)
    
    # Calculate the total number of inches the worm needs to climb
    total_inches = h - fall_inches
    
    # Calculate the number of times the worm needs to crawl up after the resting period
    num_crawls_after_rest = total_inches // a
    
    # Return the total number of crawls needed
    return num_crawls + num_crawls_after_rest


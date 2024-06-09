
def worm_climbing(a, b, h):
    # Calculate the number of times the worm needs to crawl up
    num_crawls = h // a
    
    # Calculate the number of inches the worm falls during the last crawl
    last_crawl_fall = h % a
    
    # If the worm falls during the last crawl, it needs to crawl up again
    if last_crawl_fall > b:
        num_crawls += 1
    
    return num_crawls


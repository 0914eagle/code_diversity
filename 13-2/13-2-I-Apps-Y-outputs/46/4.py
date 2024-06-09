
def worm_climbing(a, b, h):
    # Calculate the number of times the worm needs to crawl up
    num_crawls = h // a
    
    # Calculate the number of inches the worm falls during the final crawl
    final_fall = h % a
    
    # If the worm falls during the final crawl, add an additional crawl
    if final_fall > 0:
        num_crawls += 1
    
    return num_crawls


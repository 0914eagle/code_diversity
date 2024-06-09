
def solve(n, k, tabs):
    # Initialize the variables to keep track of the number of test and social network tabs
    test_tabs = 0
    social_tabs = 0
    
    # Iterate through the tabs and count the number of test and social network tabs
    for i in range(n):
        if tabs[i] == 1:
            test_tabs += 1
        else:
            social_tabs += 1
    
    # Calculate the maximum absolute difference between the amounts of remaining tabs of different types
    max_diff = abs(test_tabs - social_tabs)
    
    # Close every k-th tab and recalculate the number of test and social network tabs
    for i in range(k, n, k):
        if tabs[i] == 1:
            test_tabs -= 1
        else:
            social_tabs -= 1
        max_diff = max(max_diff, abs(test_tabs - social_tabs))
    
    return max_diff


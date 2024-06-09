
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
    
    # Iterate through the tabs and check if closing any tab would result in a higher difference
    for i in range(n):
        # Calculate the number of test and social network tabs after closing the current tab
        test_tabs_after = test_tabs - 1 if tabs[i] == 1 else test_tabs
        social_tabs_after = social_tabs - 1 if tabs[i] == -1 else social_tabs
        
        # Calculate the absolute difference between the amounts of remaining tabs of different types after closing the current tab
        diff_after = abs(test_tabs_after - social_tabs_after)
        
        # Update the maximum absolute difference if necessary
        if diff_after > max_diff:
            max_diff = diff_after
    
    return max_diff


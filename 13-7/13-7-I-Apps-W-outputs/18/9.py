
def solve(comments):
    # split the comments into a list of strings
    comments = comments.split(",")
    
    # initialize variables for the depth of nesting and the current depth
    d = 0
    current_depth = 0
    
    # initialize a dictionary to store the comments at each depth
    comments_by_depth = {}
    
    # loop through each comment
    for comment in comments:
        # check if the comment has children
        if "." in comment:
            # if it does, increment the current depth
            current_depth += 1
            # add the comment to the dictionary at the current depth
            comments_by_depth[current_depth] = comments_by_depth.get(current_depth, []) + [comment]
        else:
            # if it doesn't, set the current depth to 0
            current_depth = 0
            # add the comment to the dictionary at depth 0
            comments_by_depth[current_depth] = comments_by_depth.get(current_depth, []) + [comment]
    
    # set the maximum depth to the maximum value in the dictionary
    d = max(comments_by_depth.keys())
    
    # loop through each depth from 0 to d
    for i in range(d+1):
        # get the comments at the current depth
        comments = comments_by_depth.get(i, [])
        # join the comments with a space and print them
        print(" ".join(comments))
    
    # return the maximum depth
    return d


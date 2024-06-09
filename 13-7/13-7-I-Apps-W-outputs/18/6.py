
def solve(comments):
    # split the comments into a list of strings
    comments = comments.split(",")
    
    # initialize the depth of nesting and the levels dictionary
    depth = 0
    levels = {}
    
    # loop through each comment
    for comment in comments:
        # split the comment into its parts
        parts = comment.split()
        
        # get the level of nesting for this comment
        level = int(parts[1])
        
        # update the depth of nesting if necessary
        if level > depth:
            depth = level
        
        # add the comment to the levels dictionary
        if level not in levels:
            levels[level] = [parts[0]]
        else:
            levels[level].append(parts[0])
    
    # print the depth of nesting
    print(depth)
    
    # loop through each level of nesting
    for level in range(depth):
        # print the comments for this level
        print(" ".join(levels[level + 1]))
    
    return " ".join(levels[1])


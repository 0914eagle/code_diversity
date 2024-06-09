
def solve(comments):
    # split the comments into a list of strings
    comments = comments.split(",")
    
    # create an empty list to store the comments at each level
    levels = [[] for _ in range(10)]
    
    # iterate through the comments
    for comment in comments:
        # find the level of the current comment
        level = comment.count(",")
        
        # add the comment to the list at the corresponding level
        levels[level].append(comment)
    
    # find the maximum depth of nesting
    max_depth = len(levels) - 1
    
    # print the maximum depth
    print(max_depth)
    
    # iterate through the levels
    for level in range(max_depth):
        # print the comments at the current level
        print(" ".join(levels[level]))
    
    # print the comments at the final level
    print(" ".join(levels[max_depth]))


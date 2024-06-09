
def solve(comments):
    # split the comments into a list of strings
    comments = comments.split(",")
    
    # create an empty list to store the comments at each level
    level_comments = [[] for _ in range(10)]
    
    # iterate through the comments
    for comment in comments:
        # get the number of replies to this comment
        num_replies = int(comment.split(",")[1])
        
        # get the current level of nesting
        level = len(level_comments) - num_replies - 1
        
        # add the comment to the list at the current level
        level_comments[level].append(comment)
    
    # find the maximum depth of nesting
    max_depth = len(level_comments) - 1
    
    # create an empty list to store the formatted comments
    formatted_comments = []
    
    # iterate through the levels of nesting
    for level in range(max_depth):
        # get the comments at the current level
        level_comments = level_comments[level]
        
        # iterate through the comments at the current level
        for comment in level_comments:
            # add the comment to the formatted comments
            formatted_comments.append(comment)
    
    # return the formatted comments
    return formatted_comments


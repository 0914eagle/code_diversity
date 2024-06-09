
def solve(comments_feed):
    # split the comments feed into a list of comments
    comments = comments_feed.split(",")
    
    # create a dictionary to store the comments and their nesting level
    comment_dict = {}
    
    # iterate through the comments and add them to the dictionary with their nesting level
    for comment in comments:
        # split the comment into its text and the number of replies
        text, replies = comment.split(" ")
        
        # add the comment to the dictionary with its nesting level
        comment_dict[text] = replies
    
    # find the maximum depth of nesting
    max_depth = max(comment_dict[text] for text in comment_dict)
    
    # create a list to store the comments for each nesting level
    comments_per_level = [[] for _ in range(max_depth + 1)]
    
    # iterate through the comments and add them to the list for their nesting level
    for text, replies in comment_dict.items():
        comments_per_level[replies].append(text)
    
    # return the comments in the desired format
    return str(max_depth) + "\n" + "\n".join([" ".join(comments) for comments in comments_per_level])


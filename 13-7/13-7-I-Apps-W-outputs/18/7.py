
def solve(comments):
    # split the comments into a list of individual comments
    comments = comments.split(",")
    
    # create a dictionary to store the comments and their parents
    comment_dict = {}
    
    # iterate over the comments and add them to the dictionary
    for comment in comments:
        # split the comment into its text and the number of replies
        text, replies = comment.split(" ", 1)
        
        # add the comment to the dictionary with its replies
        comment_dict[text] = int(replies)
    
    # create a list to store the nested comments
    nested_comments = []
    
    # iterate over the comments and add them to the nested list
    for comment in comments:
        # split the comment into its text and the number of replies
        text, replies = comment.split(" ", 1)
        
        # if the comment has replies, add them to the nested list
        if int(replies) > 0:
            nested_comments.append(comment_dict[text])
    
    # return the nested comments list
    return nested_comments


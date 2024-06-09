
def solve(comments_feed):
    # split the comments feed into a list of comments
    comments = comments_feed.split(",")
    
    # create a dictionary to store the comments and their nesting level
    comment_dict = {}
    
    # iterate through the comments and add them to the dictionary with their nesting level
    for comment in comments:
        # split the comment into its parts: text, number of replies, and replies
        text, num_replies, *replies = comment.split()
        
        # add the comment to the dictionary with its nesting level
        comment_dict[text] = (num_replies, replies)
    
    # find the maximum depth of nesting in the comments
    max_depth = max(len(comment_dict[comment][1]) for comment in comment_dict)
    
    # create a list to store the comments at each nesting level
    comments_at_level = [[] for _ in range(max_depth + 1)]
    
    # iterate through the comments and add them to the list at their nesting level
    for comment in comment_dict:
        nesting_level = len(comment_dict[comment][1])
        comments_at_level[nesting_level].append(comment)
    
    # return the comments at each nesting level
    return [max_depth] + [(" ".join(comments_at_level[i])) for i in range(max_depth + 1)]


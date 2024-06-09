
def solve(comments):
    # Split the comments into a list of strings
    comments = comments.split(",")
    
    # Initialize the depth of nesting and the list of comments for each level
    depth = 0
    comments_by_level = [[] for _ in range(100)]
    
    # Iterate through the comments and add them to the appropriate level
    for comment in comments:
        # Get the number of replies for this comment
        num_replies = int(comment.split(",")[1])
        
        # Add the comment to the appropriate level
        comments_by_level[depth].append(comment)
        
        # Increment the depth if this comment has replies
        if num_replies > 0:
            depth += 1
    
    # Print the depth of nesting and the comments for each level
    print(depth)
    for level in comments_by_level:
        print(" ".join(level))


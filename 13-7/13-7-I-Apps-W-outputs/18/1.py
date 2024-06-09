
def solve(comments):
    # split the comments into a list of comments
    comments = comments.split(",")
    
    # initialize the depth of nesting and the list of comments for each level
    depth = 0
    comments_by_level = []
    
    # iterate over the comments
    for comment in comments:
        # if the comment has a parent comment, add it to the list of comments for the parent's level
        if "." in comment:
            parent_level = int(comment.split(".")[1])
            comments_by_level[parent_level].append(comment.split(".")[0])
        # if the comment is a root comment, add it to the list of comments for level 0
        else:
            comments_by_level.append([comment])
    
    # find the maximum depth of nesting
    depth = max(len(comments_by_level))
    
    # print the depth and the comments for each level
    print(depth)
    for level in range(depth):
        print(" ".join(comments_by_level[level]))



def solve(comments_feed):
    # split the comments feed into a list of comments
    comments = comments_feed.split(",")
    
    # create a dictionary to store the comments and their depth
    comments_dict = {}
    
    # loop through each comment and add it to the dictionary with its depth
    for comment in comments:
        depth = 0
        while comment[0] != " ":
            comment = comment[1:]
            depth += 1
        comments_dict[comment] = depth
    
    # find the maximum depth of nesting
    max_depth = max(comments_dict.values())
    
    # create a list to store the comments for each depth level
    comments_list = [[] for _ in range(max_depth + 1)]
    
    # loop through each comment and add it to the list of its depth level
    for comment, depth in comments_dict.items():
        comments_list[depth].append(comment)
    
    # return the results
    return str(max_depth) + "\n" + "\n".join([(" ".join(comments)) for comments in comments_list])


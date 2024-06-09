
def solve(hashtags):
    # Sort the hashtags in lexicographical order
    hashtags.sort()
    # Initialize a variable to store the total number of deleted symbols
    total_deleted = 0
    # Loop through the hashtags and check if they can be shortened
    for i in range(len(hashtags)):
        # Check if the hashtag can be shortened by deleting one or more characters from the end
        for j in range(len(hashtags[i])-1, 0, -1):
            # If the hashtag can be shortened, delete the characters and break the loop
            if hashtags[i][:j] in hashtags:
                hashtags[i] = hashtags[i][:j]
                total_deleted += len(hashtags[i]) - j
                break
    # Return the resulting hashtags and the total number of deleted symbols
    return hashtags, total_deleted


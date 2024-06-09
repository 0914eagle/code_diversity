
def solve(hashtags):
    # Sort the hashtags in lexicographical order
    hashtags.sort()
    # Initialize the total number of deleted symbols to 0
    total_deleted = 0
    # Iterate over the hashtags
    for i in range(len(hashtags)):
        # Get the current hashtag
        hashtag = hashtags[i]
        # Get the length of the hashtag
        length = len(hashtag)
        # If the hashtag is not the last one
        if i != len(hashtags) - 1:
            # Get the next hashtag
            next_hashtag = hashtags[i + 1]
            # Get the length of the next hashtag
            next_length = len(next_hashtag)
            # If the hashtag is a prefix of the next hashtag
            if hashtag == next_hashtag[:length]:
                # Delete the suffix of the hashtag
                hashtags[i] = hashtag[:length]
                # Increment the total number of deleted symbols
                total_deleted += next_length - length
    # Return the resulting hashtags and the total number of deleted symbols
    return hashtags, total_deleted


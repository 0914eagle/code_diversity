
def solve(hashtags):
    # Sort the hashtags in lexicographical order
    hashtags.sort()
    # Initialize the result list
    result = []
    # Iterate over the sorted hashtags
    for hashtag in hashtags:
        # If the hashtag is longer than 1 character
        if len(hashtag) > 1:
            # Add the shortened hashtag to the result list
            result.append(hashtag[:-1])
        # If the hashtag is 1 character long
        else:
            # Add the hashtag to the result list as is
            result.append(hashtag)
    return result


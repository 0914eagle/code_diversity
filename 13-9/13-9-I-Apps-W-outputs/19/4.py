
def solve(hashtags):
    # Sort the hashtags in lexicographical order
    hashtags.sort()
    # Initialize the result list
    result = []
    # Iterate through the sorted hashtags
    for hashtag in hashtags:
        # If the hashtag is a prefix of the previous hashtag, append the shortened hashtag to the result list
        if result and hashtag.startswith(result[-1]):
            result.append(hashtag[len(result[-1]):])
        # Otherwise, append the full hashtag to the result list
        else:
            result.append(hashtag)
    return result


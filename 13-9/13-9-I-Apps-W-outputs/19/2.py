
def solve(hashtags):
    # Sort the hashtags in lexicographical order
    sorted_hashtags = sorted(hashtags)

    # Initialize the result with the first hashtag
    result = [sorted_hashtags[0]]

    # Iterate over the remaining hashtags
    for hashtag in sorted_hashtags[1:]:
        # If the current hashtag is not a prefix of the previous hashtag, add it to the result
        if not hashtag.startswith(result[-1]):
            result.append(hashtag)

    return result


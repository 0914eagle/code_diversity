
def solve(hashtags):
    # Sort the hashtags in lexicographical order
    hashtags.sort()
    # Initialize the result and the number of deleted symbols
    result = []
    deleted_symbols = 0
    # Iterate through the hashtags
    for hashtag in hashtags:
        # If the hashtag is not '#', delete the suffixes
        if hashtag != "#":
            # Find the longest suffix that is not in lexicographical order
            i = 1
            while i < len(hashtag) and hashtag[i:] + hashtag[:i] in hashtags:
                i += 1
            # Add the hashtag with the deleted suffix to the result
            result.append(hashtag[:-i])
            # Increment the number of deleted symbols
            deleted_symbols += i
        # Otherwise, add the hashtag to the result without changes
        else:
            result.append(hashtag)
    # Return the result and the number of deleted symbols
    return result, deleted_symbols


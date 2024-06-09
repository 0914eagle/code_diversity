
def solve(hashtags):
    # Sort the hashtags in lexicographic order
    hashtags.sort()
    # Initialize the result and the number of deleted symbols
    result = []
    deleted_symbols = 0
    # Iterate over the hashtags
    for hashtag in hashtags:
        # If the hashtag is not '#', delete the suffixes
        if hashtag != "#":
            # Find the longest suffix that is not in the result
            suffix = hashtag[::-1]
            while suffix and suffix not in result:
                suffix = suffix[:-1]
            # Add the suffix to the result
            result.append(suffix)
            # Update the number of deleted symbols
            deleted_symbols += len(hashtag) - len(suffix)
        # Otherwise, add the hashtag to the result
        else:
            result.append(hashtag)
    # Return the result and the number of deleted symbols
    return result, deleted_symbols


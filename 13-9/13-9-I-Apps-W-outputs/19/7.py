
def solve(hashtags):
    # Sort the hashtags in lexicographical order
    hashtags.sort()
    # Initialize the result and the number of symbols to delete
    result = []
    num_deleted_symbols = 0
    # Loop through the hashtags
    for hashtag in hashtags:
        # If the hashtag is not '#', delete the suffix
        if hashtag != "#":
            suffix_to_delete = 1
            # Loop through the characters in the hashtag
            for i in range(len(hashtag) - 1, 0, -1):
                # If the character is different from the previous one, break
                if hashtag[i] != hashtag[i - 1]:
                    break
                # Otherwise, increment the number of symbols to delete
                suffix_to_delete += 1
            # Add the hashtag with the deleted suffix to the result
            result.append(hashtag[:-suffix_to_delete])
            # Increment the number of deleted symbols
            num_deleted_symbols += suffix_to_delete
        # Otherwise, add the hashtag to the result
        else:
            result.append(hashtag)
    # Return the result and the number of deleted symbols
    return result, num_deleted_symbols


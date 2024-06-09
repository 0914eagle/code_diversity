
def solve(hashtags):
    # Sort the hashtags in lexicographical order
    sorted_hashtags = sorted(hashtags)
    # Initialize the minimum number of characters to delete as infinite
    min_deletions = float('inf')
    # Initialize the result hashtags as an empty list
    result = []
    # Iterate over all possible combinations of hashtags
    for i in range(len(hashtags)):
        for j in range(i+1, len(hashtags)):
            # If the two hashtags are not equal and the first hashtag is a prefix of the second
            if hashtags[i] != hashtags[j] and hashtags[i].startswith(hashtags[j]):
                # Get the number of characters to delete
                deletions = len(hashtags[i]) - len(hashtags[j])
                # If the number of characters to delete is less than the minimum
                if deletions < min_deletions:
                    # Update the minimum number of characters to delete
                    min_deletions = deletions
                    # Update the result hashtags
                    result = [hashtags[i], hashtags[j]]
    # Return the result hashtags
    return result


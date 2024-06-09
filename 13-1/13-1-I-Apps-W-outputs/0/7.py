
def f1(n, hashtags):
    # Sort the hashtags in lexicographical order
    sorted_hashtags = sorted(hashtags)

    # Initialize the result with the first hashtag
    result = [sorted_hashtags[0]]

    # Iterate over the remaining hashtags
    for i in range(1, len(sorted_hashtags)):
        # Get the current hashtag and its length
        current_hashtag = sorted_hashtags[i]
        current_length = len(current_hashtag)

        # Get the previous hashtag and its length
        previous_hashtag = result[-1]
        previous_length = len(previous_hashtag)

        # If the current hashtag is not a prefix of the previous hashtag, add it to the result
        if current_hashtag[:previous_length] != previous_hashtag:
            result.append(current_hashtag)

    # Return the result
    return result

def f2(n, hashtags):
    # Initialize the result with an empty list
    result = []

    # Iterate over the hashtags
    for hashtag in hashtags:
        # Get the length of the hashtag
        length = len(hashtag)

        # If the length is 1, add the hashtag to the result
        if length == 1:
            result.append(hashtag)

        # Otherwise, add the shortest possible hashtag to the result
        else:
            result.append(hashtag[:length-1])

    # Return the result
    return result

if __name__ == '__main__':
    n = int(input())
    hashtags = [input() for _ in range(n)]
    result = f1(n, hashtags)
    print(*result, sep='\n')


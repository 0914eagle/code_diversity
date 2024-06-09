
def solve(n, friends):
    # Initialize a dictionary to map each friend to their gift
    gifts = {i: 0 for i in range(1, n+1)}

    # Iterate over the input friends and assign gifts
    for i, friend in enumerate(friends, start=1):
        if friend == 0:
            # If the friend doesn't know whom they want to give the gift to,
            # assign them a gift that is not their own
            for j in range(1, n+1):
                if j != i:
                    gifts[i] = j
                    break
        else:
            gifts[i] = friend

    # Return the gifts as a list
    return [gifts[i] for i in range(1, n+1)]


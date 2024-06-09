
def solve(n, friends):
    # Initialize a dictionary to map each friend to their gift receiver
    gift_map = {i: 0 for i in range(1, n + 1)}

    # Iterate through the input array
    for i, friend in enumerate(friends, start=1):
        # If the friend doesn't know whom they want to give the gift to, skip them
        if friend == 0:
            continue
        # If the friend knows whom they want to give the gift to, get the gift receiver's ID
        gift_receiver = friend
        # If the gift receiver has already been assigned a gift, find the next available friend as the gift receiver
        while gift_map[gift_receiver] != 0:
            gift_receiver += 1
            if gift_receiver > n:
                gift_receiver = 1
        # Assign the gift receiver to the current friend
        gift_map[i] = gift_receiver
        # Assign the current friend as the gift receiver to the gift receiver
        gift_map[gift_receiver] = i

    # Return the gift map
    return gift_map


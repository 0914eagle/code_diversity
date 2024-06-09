
def solve(n, f):
    # Initialize a dictionary to map each friend to their gift receiver
    gift_map = {}

    # Iterate through the input array
    for i in range(n):
        # If the friend knows whom they want to give the gift to
        if f[i] != 0:
            # Add the gift receiver to the dictionary
            gift_map[i] = f[i]

    # Initialize a set to store the friends who have given their gift
    given_gifts = set()

    # Iterate through the input array
    for i in range(n):
        # If the friend knows whom they want to give the gift to
        if f[i] != 0:
            # Add the friend to the set of given gifts
            given_gifts.add(i)

    # Initialize a set to store the friends who have received a gift
    received_gifts = set()

    # Iterate through the input array
    for i in range(n):
        # If the friend knows whom they want to give the gift to
        if f[i] != 0:
            # Add the friend's gift receiver to the set of received gifts
            received_gifts.add(f[i])

    # Initialize a queue to store the friends who still need to give a gift
    need_gift = deque([i for i in range(n) if f[i] == 0])

    # Iterate until the queue is empty
    while need_gift:
        # Get the next friend who still needs to give a gift
        friend = need_gift.popleft()

        # Get the list of friends who have not given a gift and are not the friend's gift receiver
        available_friends = [i for i in range(n) if i not in given_gifts and i != friend]

        # If there are no available friends, return an empty array
        if not available_friends:
            return []

        # Select a random available friend for the friend to give the gift to
        gift_receiver = available_friends[random.randint(0, len(available_friends) - 1)]

        # Add the friend and their gift receiver to the dictionary and sets
        gift_map[friend] = gift_receiver
        given_gifts.add(friend)
        received_gifts.add(gift_receiver)

        # Add the gift receiver to the queue if they still need to receive a gift
        if f[gift_receiver] == 0:
            need_gift.append(gift_receiver)

    # Return the solution
    return [gift_map[i] for i in range(n)]


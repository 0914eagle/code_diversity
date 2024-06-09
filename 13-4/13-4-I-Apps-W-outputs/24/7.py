
def is_musketeer_possible(n, m, warriors):
    # Initialize a dictionary to store the recognition of each warrior
    recognitions = {}
    for i in range(1, n + 1):
        recognitions[i] = 0

    # Iterate over the pairs of warriors knowing each other
    for i in range(m):
        # Get the two warriors knowing each other
        a, b = warriors[i]
        # Increment the recognition of each warrior by 1
        recognitions[a] += 1
        recognitions[b] += 1

    # Initialize a set to store the chosen musketeers
    musketeers = set()
    # Iterate over the warriors
    for i in range(1, n + 1):
        # If the warrior is not already in the set of musketeers and has recognition equal to 2, add it to the set
        if i not in musketeers and recognitions[i] == 2:
            musketeers.add(i)
            # If the set of musketeers has three elements, return the sum of their recognitions
            if len(musketeers) == 3:
                return sum(recognitions[i] for i in musketeers)

    # If no triple of warriors knowing each other exists, return -1
    return -1


n, m = map(int, input().split())
warriors = []
for i in range(m):
    a, b = map(int, input().split())
    warriors.append((a, b))

print(is_musketeer_possible(n, m, warriors))


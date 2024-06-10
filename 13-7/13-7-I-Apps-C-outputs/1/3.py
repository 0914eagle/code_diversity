
def get_toys(n, m, d, e, events):
    # Initialize a dictionary to store the toys played with by each kid
    toys = {i: 0 for i in range(1, n + 1)}

    # Iterate through the events
    for s, k, t in events:
        # If the kid started playing with a toy, update the dictionary
        if t != 0:
            toys[k] = t
        # If the kid stopped playing with a toy, update the dictionary
        else:
            toys[k] = 0

    # Initialize a list to store the assigned toys for each kid
    assigned_toys = []

    # Iterate through the kids
    for i in range(1, n + 1):
        # If the kid has played with a toy yesterday, assign them the same toy today
        if toys[i] != 0:
            assigned_toys.append(toys[i])
        # If the kid has not played with any toy yesterday, assign them a toy randomly
        else:
            assigned_toys.append(random.randint(1, m))

    return assigned_toys

def main():
    n, m = map(int, input().split())
    d, e = map(int, input().split())
    events = []
    for i in range(e):
        s, k, t = map(int, input().split())
        events.append((s, k, t))
    assigned_toys = get_toys(n, m, d, e, events)
    print(*assigned_toys)

if __name__ == '__main__':
    main()


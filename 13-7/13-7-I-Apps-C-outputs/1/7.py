
def get_toys(n, m, d, e, events):
    # Initialize a dictionary to store the toys played with by each kid
    toys = {}
    for event in events:
        s, k, t = event
        if t != 0:
            toys[k] = t
        else:
            toys[k] = None

    # Initialize a dictionary to store the number of times each kid played with each toy
    play_count = {}
    for k, t in toys.items():
        if t not in play_count:
            play_count[t] = {}
        play_count[t][k] = 1

    # Loop through the events and update the play count for each kid and toy
    for event in events:
        s, k, t = event
        if t != 0:
            if t not in play_count:
                play_count[t] = {}
            if k not in play_count[t]:
                play_count[t][k] = 1
            else:
                play_count[t][k] += 1

    # Sort the toys by the number of times each kid played with them
    sorted_toys = sorted(play_count.items(), key=lambda x: sum(x[1].values()), reverse=True)

    # Create a list to store the assigned toys for each kid
    assigned_toys = [None] * n

    # Loop through the sorted toys and assign them to the kids
    for t, k_count in sorted_toys:
        for k, count in k_count.items():
            if assigned_toys[k] is None:
                assigned_toys[k] = t
                break

    return assigned_toys

def main():
    n, m = map(int, input().split())
    d, e = map(int, input().split())
    events = []
    for _ in range(e):
        s, k, t = map(int, input().split())
        events.append((s, k, t))
    assigned_toys = get_toys(n, m, d, e, events)
    print(*assigned_toys)

if __name__ == '__main__':
    main()


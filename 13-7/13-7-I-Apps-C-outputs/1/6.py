
def get_assignment(n, m, d, e, events):
    # Initialize a dictionary to store the toys played with by each kid
    toys_played = {}
    for event in events:
        s, k, t = event
        if t != 0:
            toys_played[k] = t
        else:
            if k in toys_played:
                del toys_played[k]

    # Initialize a dictionary to store the number of times each kid played with each toy
    play_counts = {}
    for k, t in toys_played.items():
        if t not in play_counts:
            play_counts[t] = {}
        play_counts[t][k] = 1

    # Initialize a dictionary to store the envy of each kid for each toy
    envy = {}
    for k, t in toys_played.items():
        envy[k] = {}
        for k2, t2 in toys_played.items():
            if k2 != k and t2 == t:
                envy[k][t] = True
            else:
                envy[k][t] = False

    # Initialize a dictionary to store the inflexibility of each kid for each toy
    inflexible = {}
    for k, t in toys_played.items():
        inflexible[k] = {}
        if t in play_counts and k in play_counts[t]:
            inflexible[k][t] = play_counts[t][k]
        else:
            inflexible[k][t] = 0

    # Initialize a dictionary to store the uncooperative of each kid for each toy
    uncooperative = {}
    for k, t in toys_played.items():
        uncooperative[k] = {}
        for k2, t2 in toys_played.items():
            if k2 != k and t2 == t:
                uncooperative[k][t] = True
            else:
                uncooperative[k][t] = False

    # Initialize a dictionary to store the assigned toys for each kid
    assignments = {}
    for k in range(1, n+1):
        assignments[k] = 0

    # Iterate through the events and update the assigned toys for each kid
    for event in events:
        s, k, t = event
        if t != 0:
            if assignments[k] != 0 and assignments[k] != t:
                if envy[k][assignments[k]] and inflexible[k][assignments[k]] and uncooperative[k][assignments[k]]:
                    assignments[k] = 0
                elif envy[k][t] and inflexible[k][t] and uncooperative[k][t]:
                    assignments[k] = t
            else:
                assignments[k] = t

    # Check if there are any kids who will start crying
    for k in range(1, n+1):
        if assignments[k] == 0:
            return "impossible"

    # Return the assignments
    return [assignments[k] for k in range(1, n+1)]

def main():
    n, m = map(int, input().split())
    d, e = map(int, input().split())
    events = []
    for i in range(e):
        s, k, t = map(int, input().split())
        events.append((s, k, t))
    assignments = get_assignment(n, m, d, e, events)
    if assignments == "impossible":
        print("impossible")
    else:
        print(*assignments)

if __name__ == '__main__':
    main()


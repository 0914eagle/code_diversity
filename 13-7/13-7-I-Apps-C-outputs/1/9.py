
def get_toy_assignments(n_kids, n_toys, dur_play, events):
    # Initialize a dictionary to store the toy assignments for each kid
    toy_assignments = {}

    # Iterate through the events and update the toy assignments for each kid
    for event in events:
        kid, toy = event[1], event[2]
        if toy != 0:
            toy_assignments[kid] = toy
        else:
            toy_assignments.pop(kid, None)

    # Return the toy assignments for each kid
    return list(toy_assignments.values())

def main():
    # Read the input data
    n_kids, n_toys = map(int, input().split())
    dur_play, n_events = map(int, input().split())
    events = []
    for _ in range(n_events):
        events.append(list(map(int, input().split())))

    # Get the toy assignments for each kid
    toy_assignments = get_toy_assignments(n_kids, n_toys, dur_play, events)

    # Print the toy assignments for each kid
    print(*toy_assignments)

if __name__ == '__main__':
    main()


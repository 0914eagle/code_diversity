
def get_toy_assignment(n_kids, n_toys, play_duration, events):
    # Initialize a dictionary to store the toy assignments for each kid
    toy_assignments = {}

    # Iterate through the events and update the toy assignments for each kid
    for event in events:
        kid, toy = event[1], event[2]
        if toy != 0:
            toy_assignments[kid] = toy
        else:
            del toy_assignments[kid]

    # Check if there is a toy assignment for each kid
    if len(toy_assignments) != n_kids:
        return "impossible"

    # Check if the toy assignments are valid (i.e., no kid is playing with the same toy as another kid)
    for kid1, toy1 in toy_assignments.items():
        for kid2, toy2 in toy_assignments.items():
            if kid1 != kid2 and toy1 == toy2:
                return "impossible"

    # Return the toy assignments
    return list(toy_assignments.values())

def main():
    n_kids, n_toys = map(int, input().split())
    play_duration, n_events = map(int, input().split())
    events = []
    for _ in range(n_events):
        events.append(list(map(int, input().split())))
    print(get_toy_assignment(n_kids, n_toys, play_duration, events))

if __name__ == '__main__':
    main()


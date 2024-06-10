
def get_toy_assignments(n_kids, n_toys, duration, events):
    # Initialize a dictionary to store the toy assignments for each kid
    toy_assignments = {}

    # Iterate through the events and update the toy assignments for each kid
    for event in events:
        kid, toy = event[1], event[2]
        if kid not in toy_assignments:
            toy_assignments[kid] = toy
        elif toy_assignments[kid] != toy:
            toy_assignments[kid] = toy

    # Check if all kids have a toy assignment
    if len(toy_assignments) == n_kids:
        return list(toy_assignments.values())
    else:
        return "impossible"

def main():
    n_kids, n_toys = map(int, input().split())
    duration, n_events = map(int, input().split())
    events = []
    for _ in range(n_events):
        events.append(list(map(int, input().split())))
    print(get_toy_assignments(n_kids, n_toys, duration, events))

if __name__ == '__main__':
    main()


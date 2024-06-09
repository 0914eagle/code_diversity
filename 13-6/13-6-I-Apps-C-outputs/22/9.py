
def find_certain_events(D, M, N, implications, events):
    # Initialize a set to store the events that have certainly occurred
    certain_events = set()

    # Iterate over the given implications
    for implication in implications:
        # If the event on the right-hand side of the implication has already occurred,
        # then the event on the left-hand side of the implication must have occurred as well
        if implication[1] in certain_events:
            certain_events.add(implication[0])

    # Add the given events that have occurred to the set of certain events
    certain_events.update(events)

    # Return the set of certain events in increasing order
    return sorted(certain_events)

def main():
    # Read the input data
    D, M, N = map(int, input().split())
    implications = [tuple(map(int, input().split())) for _ in range(M)]
    events = set(map(int, input().split()))

    # Find the certain events
    certain_events = find_certain_events(D, M, N, implications, events)

    # Print the certain events in increasing order
    print(*certain_events)

if __name__ == '__main__':
    main()


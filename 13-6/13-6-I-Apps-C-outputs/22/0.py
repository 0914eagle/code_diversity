
def f1(D, M, N, implications, events):
    # Initialize a set to store the events that have certainly occurred
    certainly_occurred = set()

    # Iterate over the implications
    for implication in implications:
        # If the event that is implied by the current implication is in the set of events that have occurred,
        # then the event that caused the implication must have occurred as well
        if implication[1] in events:
            certainly_occurred.add(implication[0])

    # Return the set of events that have certainly occurred
    return certainly_occurred

def f2(D, M, N, implications, events):
    # Initialize a set to store the events that have certainly occurred
    certainly_occurred = set()

    # Iterate over the implications
    for implication in implications:
        # If the event that caused the current implication is in the set of events that have occurred,
        # then the event that is implied by the current implication must have occurred as well
        if implication[0] in events:
            certainly_occurred.add(implication[1])

    # Return the set of events that have certainly occurred
    return certainly_occurred

def main():
    # Read the input
    D, M, N = map(int, input().split())
    implications = [tuple(map(int, input().split())) for _ in range(M)]
    events = set(map(int, input().split()))

    # Find the events that have certainly occurred
    certainly_occurred = f1(D, M, N, implications, events)
    certainly_occurred = certainly_occurred.union(f2(D, M, N, implications, events))

    # Print the events that have certainly occurred
    print(*sorted(certainly_occurred), sep=' ')

if __name__ == '__main__':
    main()



def find_events(evidence, implications):
    # Initialize a set to store the events that have certainly occurred
    certainly_occurred = set()

    # Add the given evidence to the set of certainly occurred events
    certainly_occurred.update(evidence)

    # Iterate through the implications and find the events that can be deduced
    for implication in implications:
        # If the event on the left side of the implication is in the set of certainly occurred events,
        # and the event on the right side of the implication is not, then add it to the set
        if implication[0] in certainly_occurred and implication[1] not in certainly_occurred:
            certainly_occurred.add(implication[1])

    # Return the set of certainly occurred events
    return certainly_occurred

def main():
    # Read the input data
    num_events, num_implications, num_evidence = map(int, input().split())
    implications = [tuple(map(int, input().split())) for _ in range(num_implications)]
    evidence = set(map(int, input().split()))

    # Find the events that have certainly occurred
    certainly_occurred = find_events(evidence, implications)

    # Print the events that have certainly occurred
    print(*sorted(certainly_occurred), sep=' ')

if __name__ == '__main__':
    main()


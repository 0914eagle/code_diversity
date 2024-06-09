
def get_events_that_occurred(evidence, implications):
    # Initialize a set to store the events that occurred
    occurred_events = set()

    # Iterate over the evidence
    for event in evidence:
        # Add the event to the occurred events set
        occurred_events.add(event)

        # Iterate over the implications
        for implication in implications:
            # If the event is the consequence of the implication
            if event == implication[1]:
                # Add the premise of the implication to the occurred events set
                occurred_events.add(implication[0])

    # Return the occurred events set
    return occurred_events

def main():
    # Read the number of events, implications, and evidence from stdin
    num_events, num_implications, num_evidence = map(int, input().split())

    # Read the implications from stdin
    implications = []
    for _ in range(num_implications):
        premise, consequence = map(int, input().split())
        implications.append((premise, consequence))

    # Read the evidence from stdin
    evidence = set(map(int, input().split()))

    # Call the function to get the events that occurred
    occurred_events = get_events_that_occurred(evidence, implications)

    # Print the occurred events
    print(*sorted(occurred_events), sep=' ')

if __name__ == '__main__':
    main()


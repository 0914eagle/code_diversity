
def get_certain_events(evidence, implications):
    # Initialize a set to store the certain events
    certain_events = set()
    
    # Iterate over the evidence
    for event in evidence:
        # Check if the event is directly known to have occurred
        if event in implications:
            # Add the event to the set of certain events
            certain_events.add(event)
    
    # Return the set of certain events
    return certain_events

def get_possible_events(implications, certain_events):
    # Initialize a set to store the possible events
    possible_events = set()
    
    # Iterate over the implications
    for implication in implications:
        # Check if the event on the left-hand side of the implication is known to have occurred
        if implication[0] in certain_events:
            # Add the event on the right-hand side of the implication to the set of possible events
            possible_events.add(implication[1])
    
    # Return the set of possible events
    return possible_events

def get_events(implications, evidence):
    # Get the set of certain events from the evidence
    certain_events = get_certain_events(evidence, implications)
    
    # Get the set of possible events from the implications and the certain events
    possible_events = get_possible_events(implications, certain_events)
    
    # Return the set of events that are both certain and possible
    return certain_events.intersection(possible_events)

def main():
    # Read the input
    num_events, num_implications, num_evidence = map(int, input().split())
    implications = [tuple(map(int, input().split())) for _ in range(num_implications)]
    evidence = set(map(int, input().split()))
    
    # Get the set of events that are both certain and possible
    events = get_events(implications, evidence)
    
    # Print the events
    print(*sorted(events), sep=' ')

if __name__ == '__main__':
    main()


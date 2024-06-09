
def f1(D, M, N, implications, events):
    # Initialize a set to store the events that have certainly occurred
    certainly_occurred = set()

    # Iterate over the implications
    for implication in implications:
        # If the event that is implied by the implication is in the set of events that have occurred, add the event that caused the implication to the set of certainly occurred events
        if implication[1] in events:
            certainly_occurred.add(implication[0])

    # Return the set of certainly occurred events
    return certainly_occurred

def f2(D, M, N, implications, events):
    # Initialize a set to store the events that have certainly occurred
    certainly_occurred = set()

    # Iterate over the events that have occurred
    for event in events:
        # If the event is not in the set of certainly occurred events, add it to the set
        if event not in certainly_occurred:
            certainly_occurred.add(event)

    # Return the set of certainly occurred events
    return certainly_occurred

if __name__ == '__main__':
    D, M, N = map(int, input().split())
    implications = []
    events = []
    for i in range(M):
        a, b = map(int, input().split())
        implications.append((a, b))
    for i in range(N):
        x = int(input())
        events.append(x)
    certainly_occurred = f1(D, M, N, implications, events)
    print(*sorted(certainly_occurred))



def f1(D, M, N, implications, events):
    # Initialize a set to store the events that have certainly occurred
    certainly_occurred = set()

    # Iterate over the implications
    for implication in implications:
        # If the event that must have occurred (B) is in the set of events that have certainly occurred,
        # and the event that must have occurred (A) is not in the set of events that have certainly occurred,
        # then add the event that must have occurred (A) to the set of events that have certainly occurred
        if implication[1] in certainly_occurred and implication[0] not in certainly_occurred:
            certainly_occurred.add(implication[0])

    # Add the events that are known to have occurred to the set of events that have certainly occurred
    certainly_occurred.update(events)

    # Return the set of events that have certainly occurred
    return certainly_occurred

def f2(D, M, N, implications, events):
    # Initialize a set to store the events that have certainly occurred
    certainly_occurred = set()

    # Iterate over the implications
    for implication in implications:
        # If the event that must have occurred (B) is in the set of events that have certainly occurred,
        # and the event that must have occurred (A) is not in the set of events that have certainly occurred,
        # then add the event that must have occurred (A) to the set of events that have certainly occurred
        if implication[1] in certainly_occurred and implication[0] not in certainly_occurred:
            certainly_occurred.add(implication[0])

    # Add the events that are known to have occurred to the set of events that have certainly occurred
    certainly_occurred.update(events)

    # Return the set of events that have certainly occurred
    return certainly_occurred

if __name__ == '__main__':
    D, M, N = map(int, input().split())
    implications = []
    for _ in range(M):
        a, b = map(int, input().split())
        implications.append((a, b))
    events = set(map(int, input().split()))
    certainly_occurred = f1(D, M, N, implications, events)
    print(*sorted(certainly_occurred), sep=' ')


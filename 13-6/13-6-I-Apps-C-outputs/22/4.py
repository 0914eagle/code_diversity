
def solve(evidence, implications):
    # Initialize a set to store the events that have certainly occurred
    certainly_occurred = set()

    # Iterate over the evidence
    for event in evidence:
        # Add the event to the set of certainly occurred events
        certainly_occurred.add(event)

        # Iterate over the implications
        for implication in implications:
            # If the event is the antecedent of the implication
            if implication[0] == event:
                # Add the consequent of the implication to the set of certainly occurred events
                certainly_occurred.add(implication[1])

    # Return the set of certainly occurred events
    return certainly_occurred

def main():
    # Read the input
    num_events, num_implications, num_evidence = map(int, input().split())
    evidence = set(map(int, input().split()))
    implications = [tuple(map(int, input().split())) for _ in range(num_implications)]

    # Solve the problem
    certainly_occurred = solve(evidence, implications)

    # Print the result
    print(*sorted(certainly_occurred), sep='\n')

if __name__ == '__main__':
    main()


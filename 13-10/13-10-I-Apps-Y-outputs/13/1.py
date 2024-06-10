
def is_correct(proof):
    # Initialize the set of axioms
    axioms = set(["ALICE", "BOB", "CARL"])

    # Iterate through the proof lines
    for line_num, line in enumerate(proof, start=1):
        # Split the line into assumptions and conclusion
        assumptions, conclusion = line.split(" -> ")

        # Check if the conclusion is already a known axiom
        if conclusion in axioms:
            continue

        # Check if all assumptions are known axioms
        if not all(assumption in axioms for assumption in assumptions.split()):
            return line_num

        # Add the conclusion as a new axiom
        axioms.add(conclusion)

    # If all lines are correct, return "correct"
    return "correct"

def main():
    # Read the input proof
    n = int(input())
    proof = []
    for _ in range(n):
        proof.append(input())

    # Check if the proof is correct
    print(is_correct(proof))

if __name__ == '__main__':
    main()


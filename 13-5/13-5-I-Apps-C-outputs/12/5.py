
def get_disagreements(politicians):
    # Initialize a dictionary to store the disagreements
    disagreements = {}

    # Iterate over the politicians
    for i in range(len(politicians)):
        # Get the disagreements for the current politician
        disagreements[i] = set(politicians[i])

    # Iterate over the politicians again
    for i in range(len(politicians)):
        # Get the disagreements for the current politician
        current_disagreements = disagreements[i]

        # Iterate over the other politicians
        for j in range(i+1, len(politicians)):
            # Get the disagreements for the other politician
            other_disagreements = disagreements[j]

            # Update the disagreements for the current politician
            current_disagreements.update(other_disagreements)

            # Update the disagreements for the other politician
            disagreements[j] = current_disagreements

    # Return the disagreements
    return disagreements

def get_largest_committee(disagreements, k):
    # Initialize the largest committee size
    largest_committee_size = 0

    # Iterate over the politicians
    for i in range(len(disagreements)):
        # Get the disagreements for the current politician
        current_disagreements = disagreements[i]

        # Initialize the committee size
        committee_size = 1

        # Iterate over the other politicians
        for j in range(i+1, len(disagreements)):
            # Get the disagreements for the other politician
            other_disagreements = disagreements[j]

            # Check if the current politician disagrees with the other politician
            if i in other_disagreements and j not in current_disagreements:
                # Add the other politician to the committee
                current_disagreements.add(j)
                committee_size += 1

        # Check if the committee size is larger than the largest committee size
        if committee_size > largest_committee_size:
            # Update the largest committee size
            largest_committee_size = committee_size

    # Return the largest committee size
    return largest_committee_size

def main():
    # Read the input
    n, k = map(int, input().split())
    politicians = [set(map(int, input().split())) for _ in range(n)]

    # Get the disagreements
    disagreements = get_disagreements(politicians)

    # Get the largest committee size
    largest_committee_size = get_largest_committee(disagreements, k)

    # Print the largest committee size
    print(largest_committee_size)

if __name__ == '__main__':
    main()


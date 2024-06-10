
def get_minimum_inspectors(n, d):
    # Initialize a list to store the number of inspectors needed for each tree
    inspectors_needed = [0] * (n + 1)

    # Iterate through each tree and calculate the number of inspectors needed for that tree
    for i in range(1, n + 1):
        # Calculate the range of trees that the inspector under the current tree will inspect
        inspect_range = list(range(i - d, i + d + 1))

        # Remove the current tree from the range, since it will be inspected by the inspector under it
        inspect_range.remove(i)

        # Add the number of inspectors needed for the trees in the range to the total number of inspectors needed for the current tree
        inspectors_needed[i] = sum(inspectors_needed[tree] for tree in inspect_range) + 1

    # Return the maximum number of inspectors needed across all trees
    return max(inspectors_needed)

def main():
    n, d = map(int, input().split())
    print(get_minimum_inspectors(n, d))

if __name__ == '__main__':
    main()


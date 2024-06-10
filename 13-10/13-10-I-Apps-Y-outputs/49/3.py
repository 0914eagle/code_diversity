
def get_min_inspectors(n, d):
    # Calculate the maximum number of inspectors needed to cover all trees
    max_inspectors = (n + d) // d
    # Initialize a list to store the inspectors and their corresponding trees
    inspectors = [[] for _ in range(max_inspectors)]
    # Loop through each tree and assign an inspector to it
    for i in range(n):
        # Calculate the inspector index based on the tree index and the distance between inspectors
        inspector_index = (i // d) % max_inspectors
        # Add the tree to the inspector's list of trees
        inspectors[inspector_index].append(i)
    # Loop through each inspector and count the number of trees they are responsible for
    inspector_counts = [len(inspector) for inspector in inspectors]
    # Return the minimum number of inspectors needed to cover all trees
    return min(inspector_counts)

def main():
    n, d = map(int, input().split())
    print(get_min_inspectors(n, d))

if __name__ == '__main__':
    main()



def get_min_inspectors(N, D):
    # Calculate the maximum number of inspectors needed to inspect all trees
    max_inspectors = (N + D - 1) // D
    # Initialize a list to store the inspectors and their corresponding trees
    inspectors = []
    # Loop through each tree and add the inspectors that can inspect it to the list
    for i in range(1, N + 1):
        inspectors.append([i, i + D])
    # Sort the list by the inspector's tree number in ascending order
    inspectors.sort(key=lambda x: x[0])
    # Initialize a variable to store the minimum number of inspectors needed
    min_inspectors = 0
    # Loop through each inspector and check if it can inspect all the trees
    for i in range(len(inspectors)):
        # Check if the inspector can inspect all the trees between its tree number and the previous inspector's tree number
        if inspectors[i][0] - inspectors[i - 1][1] > 1:
            # If the inspector cannot inspect all the trees, increment the minimum number of inspectors needed
            min_inspectors += 1
        # If the inspector can inspect all the trees, break the loop
        if min_inspectors == max_inspectors:
            break
    return min_inspectors

def main():
    N, D = map(int, input().split())
    print(get_min_inspectors(N, D))

if __name__ == '__main__':
    main()


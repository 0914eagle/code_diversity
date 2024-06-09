
def get_finalists(results, k):
    # Sort the results in ascending order
    results.sort()
    # Initialize the finalists list
    finalists = []
    # Add the top k results from each semifinal to the finalists list
    for i in range(k):
        finalists.append(results[i])
        finalists.append(results[i + k])
    # Add the remaining results to the finalists list
    for i in range(2 * k, len(results)):
        finalists.append(results[i])
    # Return the finalists list
    return finalists

def get_finalists_indices(results, k):
    # Get the finalists list
    finalists = get_finalists(results, k)
    # Initialize the finalists indices list
    finalists_indices = []
    # Add the indices of the finalists to the finalists indices list
    for i in range(len(results)):
        if results[i] in finalists:
            finalists_indices.append(i)
    # Return the finalists indices list
    return finalists_indices

def get_finalists_string(results, k):
    # Get the finalists indices list
    finalists_indices = get_finalists_indices(results, k)
    # Initialize the finalists string
    finalists_string = ""
    # Add the finalists indices to the finalists string
    for i in range(len(results)):
        if i in finalists_indices:
            finalists_string += "1"
        else:
            finalists_string += "0"
    # Return the finalists string
    return finalists_string

def main():
    # Read the input
    n = int(input())
    results = []
    for i in range(n):
        results.append(int(input()))
    # Get the finalists string
    finalists_string = get_finalists_string(results, k)
    # Print the finalists string
    print(finalists_string)

if __name__ == '__main__':
    main()


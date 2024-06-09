
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
    for i in range(k, len(results)):
        finalists.append(results[i])
    # Return the finalists list
    return finalists

def get_chances(results, k):
    # Sort the results in ascending order
    results.sort()
    # Initialize the chances list
    chances = []
    # Add a "1" to the chances list for the top k results from each semifinal
    for i in range(k):
        chances.append(1)
        chances.append(1)
    # Add a "0" to the chances list for the remaining results
    for i in range(k, len(results)):
        chances.append(0)
    # Return the chances list
    return chances

def main():
    # Read the number of participants and the results from stdin
    n = int(input())
    results = []
    for i in range(n):
        results.append(int(input()))
    # Call the get_finalists function to get the finalists list
    finalists = get_finalists(results, k)
    # Call the get_chances function to get the chances list
    chances = get_chances(results, k)
    # Print the finalists list
    print(" ".join(map(str, finalists)))
    # Print the chances list
    print(" ".join(map(str, chances)))

if __name__ == '__main__':
    main()


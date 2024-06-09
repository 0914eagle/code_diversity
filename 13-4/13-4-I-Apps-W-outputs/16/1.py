
def get_finalists(results, k):
    # Sort the results in ascending order
    results.sort()
    
    # Find the kth smallest element in the results
    kth_smallest = results[k]
    
    # Find the index of the kth smallest element in the results
    kth_index = results.index(kth_smallest)
    
    # Get the finalists by finding the first k elements that are not the kth smallest element
    finalists = results[:k]
    
    # Add the remaining elements that are not the kth smallest element
    for i in range(k, len(results)):
        if results[i] != kth_smallest:
            finalists.append(results[i])
    
    return finalists

def get_chances(results, k):
    # Get the finalists
    finalists = get_finalists(results, k)
    
    # Initialize the chances array
    chances = [0] * len(results)
    
    # Set the chances for the finalists to 1
    for i in range(len(finalists)):
        chances[finalists[i]] = 1
    
    return chances

def main():
    # Read the input
    n = int(input())
    results = []
    for i in range(n):
        results.append(int(input()))
    
    # Get the chances for each participant
    chances = get_chances(results, k)
    
    # Print the chances
    for i in range(len(chances)):
        print(chances[i], end="")

if __name__ == '__main__':
    main()


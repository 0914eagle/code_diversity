
def get_finalists(results, k):
    # Sort the results in ascending order
    results.sort()
    
    # Find the kth smallest element in the results
    kth_smallest = results[k]
    
    # Find the index of the kth smallest element in the results
    kth_index = results.index(kth_smallest)
    
    # Find the number of participants in each semifinal
    n = len(results) // 2
    
    # Initialize the finalists array
    finalists = [0] * n
    
    # Fill the finalists array with the winners from each semifinal
    for i in range(n):
        finalists[i] = results[i]
    
    # Fill the remaining places in the finalists array with the participants who didn't make it to the top k in their semifinal but have the best time among the others
    for i in range(n, n - k):
        finalists[i] = results[kth_index + i - n + 1]
    
    return finalists

def main():
    n = int(input())
    results = []
    for i in range(n):
        results.append(int(input()))
    k = int(input())
    finalists = get_finalists(results, k)
    print(" ".join(str(finalist) for finalist in finalists))

if __name__ == '__main__':
    main()


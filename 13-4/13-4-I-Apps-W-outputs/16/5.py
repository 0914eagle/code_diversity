
def get_finalists(results, k):
    # Sort the results in ascending order
    results.sort()
    # Find the kth smallest element
    kth_smallest = results[k]
    # Find the index of the kth smallest element
    kth_index = results.index(kth_smallest)
    # Get the finalists by slicing the list from the beginning to the kth index
    finalists = results[:kth_index]
    return finalists

def get_chances(results, k):
    # Get the finalists
    finalists = get_finalists(results, k)
    # Get the number of finalists
    n_finalists = len(finalists)
    # Get the number of participants
    n_participants = len(results)
    # Initialize an array to store the chances
    chances = [0] * n_participants
    # Loop through the participants
    for i in range(n_participants):
        # If the participant is a finalist, they have a chance to advance
        if results[i] in finalists:
            chances[i] = 1
        # If the participant is not a finalist, they have a chance to advance if there are still spots available
        elif n_finalists < n_participants:
            chances[i] = 1
    return chances

def main():
    n = int(input())
    results = []
    for i in range(n):
        results.append(int(input()))
    k = int(input())
    chances = get_chances(results, k)
    print(" ".join(map(str, chances)))

if __name__ == '__main__':
    main()


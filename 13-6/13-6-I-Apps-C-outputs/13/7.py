
import itertools

def f1(n, a):
    # Calculate the number of permutations of the input sequence
    num_permutations = math.factorial(n)
    
    # Initialize a counter for the number of entirely unsorted sequences
    num_entirely_unsorted = 0
    
    # Iterate over all permutations of the input sequence
    for permutation in itertools.permutations(a):
        # Check if the current permutation is entirely unsorted
        if is_entirely_unsorted(permutation):
            num_entirely_unsorted += 1
    
    # Return the number of entirely unsorted sequences modulo 10^9 + 9
    return num_entirely_unsorted % (10**9 + 9)

def is_entirely_unsorted(permutation):
    # Initialize a flag to indicate if the current permutation is entirely unsorted
    is_unsorted = True
    
    # Iterate over all elements in the permutation
    for i in range(len(permutation)):
        # If any element is sorted, set the flag to False and break the loop
        if is_sorted(permutation, i):
            is_unsorted = False
            break
    
    # Return the flag indicating if the current permutation is entirely unsorted
    return is_unsorted

def is_sorted(permutation, i):
    # Initialize a flag to indicate if the current element is sorted
    is_sorted = True
    
    # Iterate over all elements after the current element
    for j in range(i+1, len(permutation)):
        # If any element after the current element is less than the current element, set the flag to False and break the loop
        if permutation[j] < permutation[i]:
            is_sorted = False
            break
    
    # Return the flag indicating if the current element is sorted
    return is_sorted

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))


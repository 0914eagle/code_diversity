
def get_sorted_permutation(p):
    n = len(p)
    # Initialize the number of swaps to 0
    num_swaps = 0
    # Loop through each element in the permutation
    for i in range(n):
        # Find the index of the element that is two indices away from the current element
        j = i + 2
        # If the element at the found index is smaller than the current element, swap them
        if j < n and p[j] < p[i]:
            p[i], p[j] = p[j], p[i]
            num_swaps += 1
    return p, num_swaps

def get_swaps(p):
    n = len(p)
    # Initialize the number of swaps to 0
    num_swaps = 0
    # Loop through each element in the permutation
    for i in range(n):
        # Find the index of the element that is two indices away from the current element
        j = i + 2
        # If the element at the found index is smaller than the current element, swap them
        if j < n and p[j] < p[i]:
            num_swaps += 1
    return num_swaps

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p, num_swaps = get_sorted_permutation(p)
    print(num_swaps)
    for i in range(num_swaps):
        print(i+1, i+2)

if __name__ == '__main__':
    main()


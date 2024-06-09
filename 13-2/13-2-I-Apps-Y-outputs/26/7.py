
def can_sort_permutation(permutation):
    
    # Sort the permutation in ascending order
    sorted_permutation = sorted(permutation)
    # Check if the sorted permutation is the same as the original permutation
    return permutation == sorted_permutation

def main():
    # Read the input from stdin
    N = int(input())
    permutation = list(map(int, input().split()))
    # Check if the permutation can be sorted
    if can_sort_permutation(permutation):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()


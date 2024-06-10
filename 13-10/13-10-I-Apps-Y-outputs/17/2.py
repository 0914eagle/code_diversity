
import sys

def get_lexicographical_index(permutation):
    # Calculate the lexicographical index of the permutation
    index = 1
    for i in range(1, len(permutation)):
        for j in range(i, len(permutation)):
            if permutation[i] < permutation[j]:
                index += 1
    return index

def get_absolute_difference(permutation1, permutation2):
    # Calculate the absolute difference between the two lexicographical indices
    index1 = get_lexicographical_index(permutation1)
    index2 = get_lexicographical_index(permutation2)
    return abs(index1 - index2)

def main():
    # Read the input from stdin
    N = int(input())
    permutation1 = list(map(int, input().split()))
    permutation2 = list(map(int, input().split()))

    # Calculate the absolute difference between the two permutations
    difference = get_absolute_difference(permutation1, permutation2)

    # Print the result
    print(difference)

if __name__ == '__main__':
    main()


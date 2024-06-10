
def get_permutation_beauty(permutation):
    # Calculate the beauty of the permutation
    beauty = 0
    for i in range(len(permutation)):
        beauty += (i ^ permutation[i])
    return beauty

def get_maximum_beauty_permutation(n):
    # Generate all permutations of numbers from 0 to n
    permutations = []
    for i in range(n+1):
        permutations.append(i)
    permutations = list(itertools.permutations(permutations))

    # Find the permutation with the maximum beauty
    maximum_beauty = 0
    maximum_beauty_permutation = []
    for permutation in permutations:
        beauty = get_permutation_beauty(permutation)
        if beauty > maximum_beauty:
            maximum_beauty = beauty
            maximum_beauty_permutation = permutation

    return maximum_beauty, maximum_beauty_permutation

def main():
    n = int(input())
    maximum_beauty, maximum_beauty_permutation = get_maximum_beauty_permutation(n)
    print(maximum_beauty)
    print(*maximum_beauty_permutation)

if __name__ == '__main__':
    main()


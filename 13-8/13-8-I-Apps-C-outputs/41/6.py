
def riffle_shuffle(n):
    # Initialize a list to store the shuffle count for each permutation
    shuffle_count = [0] * (n + 1)
    
    # Iterate over all permutations of the deck
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # If the current permutation is the identity permutation, set the shuffle count to 0
            if i == j:
                shuffle_count[i] = 0
            # Otherwise, find the minimum number of shuffles required to get from the current permutation to the identity permutation
            else:
                shuffle_count[i] = min(shuffle_count[i], shuffle_count[j] + 1)
    
    return shuffle_count[n]

def main():
    n = int(input())
    deck = list(map(int, input().split()))
    print(riffle_shuffle(n))

if __name__ == '__main__':
    main()


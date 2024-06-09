
def get_magical_permutation(S):
    # Function to find the largest non-negative integer x such that there is a magical permutation of integers from 0 to 2^x - 1
    x = 0
    while True:
        permutation = get_permutation(x)
        if all(permutation[i] ^ permutation[i+1] in S for i in range(len(permutation)-1)):
            return x, permutation
        x += 1

def get_permutation(x):
    # Function to generate a permutation of integers from 0 to 2^x - 1
    permutation = []
    for i in range(2**x):
        permutation.append(i)
    return permutation

def main():
    n = int(input())
    S = set(map(int, input().split()))
    x, permutation = get_magical_permutation(S)
    print(x)
    print(*permutation)

if __name__ == '__main__':
    main()


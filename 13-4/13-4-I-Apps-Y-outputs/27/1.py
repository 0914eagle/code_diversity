
def get_smallest_integers(A, B, K):
    smallest_integers = []
    for i in range(A, B+1):
        if i <= K:
            smallest_integers.append(i)
    return smallest_integers

def get_largest_integers(A, B, K):
    largest_integers = []
    for i in range(A, B+1):
        if i >= B-K+1:
            largest_integers.append(i)
    return largest_integers

def get_all_integers(A, B, K):
    smallest_integers = get_smallest_integers(A, B, K)
    largest_integers = get_largest_integers(A, B, K)
    return smallest_integers + largest_integers

if __name__ == '__main__':
    A, B, K = map(int, input().split())
    all_integers = get_all_integers(A, B, K)
    print(*all_integers, sep='\n')


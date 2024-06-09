
def get_input():
    return list(map(int, input().split()))

def get_sorted_integers(A, B, K):
    sorted_integers = []
    for i in range(A, B+1):
        if i in range(A, A+K) or i in range(B-K+1, B+1):
            sorted_integers.append(i)
    return sorted_integers

def main():
    A, B, K = get_input()
    sorted_integers = get_sorted_integers(A, B, K)
    print(*sorted_integers, sep='\n')

if __name__ == '__main__':
    main()


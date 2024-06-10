
def get_valid_permutations(A, B):
    n = len(A)
    valid_permutations = 0
    for i in range(n):
        for j in range(i+1, n+1):
            if A[i:j] == B[i:j]:
                valid_permutations += 1
    return valid_permutations

def main():
    A = input()
    B = input()
    print(get_valid_permutations(A, B))

if __name__ == '__main__':
    main()



def get_input():
    N = int(input())
    L = list(map(int, input().split()))
    return N, L

def find_triples(N, L):
    triples = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                    triples += 1
    return triples

def main():
    N, L = get_input()
    print(find_triples(N, L))

if __name__ == '__main__':
    main()



def read_input():
    L1, L2, N = map(int, input().split())
    tubes = [int(input()) for _ in range(N)]
    return L1, L2, N, tubes

def get_max_length(L1, L2, N, tubes):
    tubes.sort(reverse=True)
    for i in range(N-1):
        for j in range(i+1, N):
            if tubes[i] + tubes[j] <= L1 and tubes[i+j] + tubes[j+1] <= L2:
                return tubes[i] + tubes[j] + tubes[i+j] + tubes[j+1]
    return "Impossible"

if __name__ == '__main__':
    L1, L2, N, tubes = read_input()
    print(get_max_length(L1, L2, N, tubes))


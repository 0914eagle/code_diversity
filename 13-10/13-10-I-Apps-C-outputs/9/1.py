
def read_input():
    L1, L2, N = map(int, input().split())
    tubes = [int(input()) for _ in range(N)]
    return L1, L2, tubes

def get_max_total_length(L1, L2, tubes):
    tubes.sort(reverse=True)
    total_length = 0
    for i in range(2):
        for j in range(i+2, 4):
            if tubes[i] + tubes[j] <= L1 and tubes[i+1] + tubes[j-1] <= L2:
                total_length += tubes[i] + tubes[j] + tubes[i+1] + tubes[j-1]
                return total_length
    return "Impossible"

if __name__ == '__main__':
    L1, L2, tubes = read_input()
    print(get_max_total_length(L1, L2, tubes))


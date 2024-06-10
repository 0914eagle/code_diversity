
def get_input():
    N = int(input())
    cheetahs = []
    for i in range(N):
        t, v = map(int, input().split())
        cheetahs.append((t, v))
    return N, cheetahs

def solve(N, cheetahs):
    cheetahs.sort(key=lambda x: x[0])
    min_length = float('inf')
    for i in range(N):
        t, v = cheetahs[i]
        for j in range(i+1, N):
            t_j, v_j = cheetahs[j]
            length = (t_j - t) * v_j + (v - v_j) * (t - t_j) / (v - v_j)
            min_length = min(min_length, length)
    return min_length

def main():
    N, cheetahs = get_input()
    print(solve(N, cheetahs))

if __name__ == '__main__':
    main()


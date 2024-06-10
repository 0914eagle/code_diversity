
def get_input():
    N = int(input())
    cheetahs = []
    for _ in range(N):
        t, v = map(int, input().split())
        cheetahs.append((t, v))
    return N, cheetahs

def get_min_length(N, cheetahs):
    cheetahs.sort(key=lambda x: x[0])
    min_length = float('inf')
    for i in range(N):
        t, v = cheetahs[i]
        for j in range(i+1, N):
            t2, v2 = cheetahs[j]
            if t2 - t <= v * (j - i):
                min_length = min(min_length, j - i)
    return min_length

def main():
    N, cheetahs = get_input()
    print(get_min_length(N, cheetahs))

if __name__ == '__main__':
    main()


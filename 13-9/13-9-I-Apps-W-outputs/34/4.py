
def get_strength(a, b):
    return a + b

def get_teammate(strengths, n):
    teammates = [0] * (n + 1)
    for i in range(1, n + 1):
        max_strength = 0
        for j in range(1, n + 1):
            if i != j and strengths[i][j] > max_strength:
                max_strength = strengths[i][j]
                teammates[i] = j
    return teammates

def main():
    n = int(input())
    strengths = []
    for i in range(n):
        strengths.append(list(map(int, input().split())))
    teammates = get_teammate(strengths, n)
    print(*teammates)

if __name__ == '__main__':
    main()


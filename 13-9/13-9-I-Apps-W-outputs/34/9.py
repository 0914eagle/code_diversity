
def get_teammates(strengths):
    n = len(strengths)
    teammates = [0] * n
    for i in range(n):
        max_strength = 0
        for j in range(n):
            if i != j and strengths[i][j] > max_strength:
                max_strength = strengths[i][j]
                teammates[i] = j + 1
    return teammates

def main():
    n = int(input())
    strengths = []
    for i in range(n):
        strengths.append(list(map(int, input().split())))
    teammates = get_teammates(strengths)
    print(*teammates)

if __name__ == '__main__':
    main()


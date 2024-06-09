
def get_correct_codes(n, m, c, b, a):
    correct_codes = 0
    for i in range(n):
        sum = 0
        for j in range(m):
            sum += a[i][j] * b[j]
        sum += c
        if sum > 0:
            correct_codes += 1
    return correct_codes

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    print(get_correct_codes(n, m, c, b, a))

if __name__ == '__main__':
    main()


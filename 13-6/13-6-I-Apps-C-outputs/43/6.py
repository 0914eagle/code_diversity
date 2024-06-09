
def f1(N, v):
    # calculate the expected value for each hole
    expected_values = [0] * (N * (N + 1) // 2)
    for i in range(N * (N + 1) // 2):
        expected_values[i] = v[i]
        for j in range(i + 1, N * (N + 1) // 2):
            if i % N != 0 and j % N != 0:
                expected_values[i] += 0.25 * v[j]
            elif i % N != 0:
                expected_values[i] += 0.5 * v[j]
            elif j % N != 0:
                expected_values[i] += 0.5 * v[j]
            else:
                expected_values[i] += v[j]
    return expected_values

def f2(N, v, p):
    # calculate the expected value for each hole after bouncing once
    expected_values = [0] * (N * (N + 1) // 2)
    for i in range(N * (N + 1) // 2):
        expected_values[i] = v[i]
        for j in range(i + 1, N * (N + 1) // 2):
            if i % N != 0 and j % N != 0:
                expected_values[i] += 0.25 * p[i][j] * v[j]
            elif i % N != 0:
                expected_values[i] += 0.5 * p[i][j] * v[j]
            elif j % N != 0:
                expected_values[i] += 0.5 * p[i][j] * v[j]
            else:
                expected_values[i] += p[i][j] * v[j]
    return expected_values

def f3(N, v, p, b):
    # calculate the expected value for each hole after bouncing b times
    expected_values = [0] * (N * (N + 1) // 2)
    for i in range(N * (N + 1) // 2):
        expected_values[i] = v[i]
        for j in range(i + 1, N * (N + 1) // 2):
            if i % N != 0 and j % N != 0:
                expected_values[i] += (0.25 * p[i][j]) ** b * v[j]
            elif i % N != 0:
                expected_values[i] += (0.5 * p[i][j]) ** b * v[j]
            elif j % N != 0:
                expected_values[i] += (0.5 * p[i][j]) ** b * v[j]
            else:
                expected_values[i] += p[i][j] ** b * v[j]
    return expected_values

def main():
    N = int(input())
    v = list(map(int, input().split()))
    p = []
    for i in range(N * (N + 1) // 2):
        p.append(list(map(float, input().split())))
    b = int(input())
    expected_values = f1(N, v)
    for i in range(b):
        expected_values = f2(N, expected_values, p)
    print(sum(expected_values))

if __name__ == '__main__':
    main()


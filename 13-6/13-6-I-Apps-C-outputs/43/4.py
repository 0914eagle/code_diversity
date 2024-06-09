
def f1(N, v, p):
    # Calculate the expected value for each hole
    expected_values = [0] * (N * (N + 1) // 2)
    for i in range(N * (N + 1) // 2):
        expected_values[i] = v[i] + p[i] * (expected_values[i] if i == 0 else expected_values[i - 1])
    
    # Calculate the expected value for the entire machine
    return sum(expected_values)

def f2(N, v, p):
    # Calculate the expected value for each hole
    expected_values = [0] * (N * (N + 1) // 2)
    for i in range(N * (N + 1) // 2):
        expected_values[i] = v[i] + p[i] * (expected_values[i] if i == 0 else expected_values[i - 1])
    
    # Calculate the expected value for the entire machine
    return sum(expected_values)

if __name__ == '__main__':
    N = int(input())
    v = list(map(int, input().split()))
    p = []
    for i in range(N * (N + 1) // 2):
        p.append(list(map(float, input().split())))
    
    print(f1(N, v, p))
    print(f2(N, v, p))


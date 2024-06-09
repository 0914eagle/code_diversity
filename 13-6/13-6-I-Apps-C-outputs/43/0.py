
def f1(N, H, v, p):
    # Calculate the expected value for each hole
    expected_values = [0] * (H + 1)
    for i in range(H):
        expected_values[i] = v[i] + p[i] * expected_values[i + 1]
    
    # Calculate the expected value for the top hole
    expected_values[H] = v[H] + p[H] * expected_values[1]
    
    return expected_values[1]

def f2(N, H, v, p):
    # Calculate the expected value for each hole
    expected_values = [0] * (H + 1)
    for i in range(H):
        expected_values[i] = v[i] + p[i] * expected_values[i + 1]
    
    # Calculate the expected value for the top hole
    expected_values[H] = v[H] + p[H] * expected_values[1]
    
    return expected_values[1]

if __name__ == '__main__':
    N = int(input())
    H = N * (N + 1) // 2
    v = list(map(int, input().split()))
    p = []
    for i in range(H):
        p.append(list(map(float, input().split())))
    
    print(f1(N, H, v, p))
    print(f2(N, H, v, p))


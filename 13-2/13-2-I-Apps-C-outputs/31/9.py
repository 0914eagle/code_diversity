
def f1(S):
    # Calculate the average value of L(C) over all possible sequences C represented by S
    n = len(S)
    count = 0
    sum = 0
    for i in range(1, n+1):
        for j in range(n-i+1):
            C = S[j:j+i]
            count += 1
            sum += calculate_L(C)
    return sum / count

def calculate_L(C):
    # Calculate the number of operations before Prof. Tuy stops for a given initial configuration C
    n = len(C)
    if n == 1:
        return 1
    if C[0] == 'H':
        return 1 + calculate_L(C[1:])
    if C[0] == 'T':
        return 1 + calculate_L(C[1:])
    if C[0] == '?':
        return 1 + calculate_L(C[1:])

if __name__ == '__main__':
    S = input()
    print(f1(S))



def get_base_f_solution(B, N):
    if B < 2 or B > 10000:
        return "impossible"
    
    if N < 0 or N >= 2**63:
        return "impossible"
    
    for X in range(1, 2**63):
        if f_B(X, B) == N:
            return X
    
    return "impossible"

def f_B(X, B):
    if X < 0 or X >= 2**63:
        return "impossible"
    
    result = 0
    while X > 0:
        result += (X % B) * (X % B)
        X //= B
    
    return result

if __name__ == '__main__':
    B, N = map(int, input().split())
    print(get_base_f_solution(B, N))


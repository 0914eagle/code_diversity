
def get_arithmetic_progression(L, A, B, M):
    # Calculate the sum of the arithmetic progression
    sum = (L * (2 * A + (L - 1) * B)) // 2
    
    # Calculate the remainder when the sum is divided by M
    remainder = sum % M
    
    return remainder

def main():
    L, A, B, M = map(int, input().split())
    print(get_arithmetic_progression(L, A, B, M))

if __name__ == '__main__':
    main()


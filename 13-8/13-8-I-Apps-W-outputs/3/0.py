
def get_remainder(L, A, B, M):
    # Calculate the sum of the terms in the arithmetic progression
    sum = (L * (L + 1)) // 2 * A
    
    # Calculate the product of the terms in the arithmetic progression
    product = (L * (L + 1)) // 2 * A ** 2
    
    # Calculate the remainder when the product is divided by M
    remainder = product % M
    
    return remainder

def main():
    L, A, B, M = map(int, input().split())
    print(get_remainder(L, A, B, M))

if __name__ == '__main__':
    main()


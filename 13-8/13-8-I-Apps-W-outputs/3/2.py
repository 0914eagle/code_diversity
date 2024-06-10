
def get_remainder(L, A, B, M):
    # Calculate the sum of the terms in the arithmetic progression
    sum_terms = (L * (L + 1)) // 2
    
    # Calculate the product of the terms in the arithmetic progression
    prod_terms = 1
    for i in range(L):
        prod_terms *= A + B * i
    
    # Calculate the remainder when the product of the terms is divided by M
    remainder = prod_terms % M
    
    return remainder

def main():
    L, A, B, M = map(int, input().split())
    print(get_remainder(L, A, B, M))

if __name__ == '__main__':
    main()


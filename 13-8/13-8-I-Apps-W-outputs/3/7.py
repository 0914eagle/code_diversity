
def concatenate_terms(terms):
    return int(''.join(map(str, terms)))

def arithmetic_progression_remainder(L, A, B, M):
    terms = [A + B * i for i in range(L)]
    return concatenate_terms(terms) % M

def main():
    L, A, B, M = map(int, input().split())
    print(arithmetic_progression_remainder(L, A, B, M))

if __name__ == '__main__':
    main()


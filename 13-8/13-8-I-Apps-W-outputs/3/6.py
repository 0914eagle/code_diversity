
def get_arithmetic_progression(L, A, B, M):
    prog = [A + B * i for i in range(L)]
    concat = int("".join(map(str, prog)))
    return concat % M

def main():
    L, A, B, M = map(int, input().split())
    print(get_arithmetic_progression(L, A, B, M))

if __name__ == '__main__':
    main()


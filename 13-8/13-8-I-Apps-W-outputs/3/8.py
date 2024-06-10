
def get_arithmetic_progression(L, A, B, M):
    progression = [A + B * i for i in range(L)]
    concatenated = int("".join(str(x) for x in progression))
    return concatenated % M

def main():
    L, A, B, M = map(int, input().split())
    print(get_arithmetic_progression(L, A, B, M))

if __name__ == '__main__':
    main()


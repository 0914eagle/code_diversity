
def get_arithmetic_progression(L, A, B):
    return [A + B * i for i in range(L)]

def get_concatenated_integer(progression):
    return int(''.join(map(str, progression)))

def get_remainder(progression, M):
    return get_concatenated_integer(progression) % M

def main():
    L, A, B, M = map(int, input().split())
    progression = get_arithmetic_progression(L, A, B)
    print(get_remainder(progression, M))

if __name__ == '__main__':
    main()


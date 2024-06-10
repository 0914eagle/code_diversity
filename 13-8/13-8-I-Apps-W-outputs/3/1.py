
def get_arithmetic_progression(L, A, B):
    progression = []
    for i in range(L):
        progression.append(A + B * i)
    return progression

def get_concatenated_number(progression):
    concatenated_number = ''
    for term in progression:
        concatenated_number += str(term)
    return concatenated_number

def get_remainder(concatenated_number, M):
    return int(concatenated_number) % M

def main():
    L, A, B, M = map(int, input().split())
    progression = get_arithmetic_progression(L, A, B)
    concatenated_number = get_concatenated_number(progression)
    remainder = get_remainder(concatenated_number, M)
    print(remainder)

if __name__ == '__main__':
    main()


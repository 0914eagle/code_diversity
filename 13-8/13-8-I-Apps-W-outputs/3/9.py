
def get_arithmetic_progression(L, A, B):
    prog = []
    for i in range(L):
        prog.append(A + B * i)
    return prog

def concatenate_terms(prog):
    concat = ""
    for term in prog:
        concat += str(term)
    return concat

def get_remainder(concat, M):
    return int(concat) % M

if __name__ == '__main__':
    L, A, B, M = map(int, input().split())
    prog = get_arithmetic_progression(L, A, B)
    concat = concatenate_terms(prog)
    remainder = get_remainder(concat, M)
    print(remainder)


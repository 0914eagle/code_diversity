
def solve(equation):
    A, S = equation.split('=')
    A = A.strip()
    S = S.strip()
    A_list = list(A)
    S_list = list(S)
    for i in range(len(A_list)):
        if A_list[i] != S_list[i]:
            A_list.insert(i, '+')
    return ''.join(A_list)


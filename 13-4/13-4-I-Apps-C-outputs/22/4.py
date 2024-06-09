
def solve(N, L_R_list):
    expected_payment = 0
    for i in range(N):
        L, R = L_R_list[i]
        expected_payment += (R - L) / 2
    return expected_payment / (N ** 2)


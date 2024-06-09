
def solve(N, salaries):
    expected_payment = 0
    for i in range(N):
        for j in range(i+1, N):
            if salaries[i] > salaries[j]:
                expected_payment += salaries[i] - salaries[j]
    return expected_payment / N ** 2


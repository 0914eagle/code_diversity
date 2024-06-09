
def solve(N, salaries):
    expected_damages = 0
    for i in range(N):
        for j in range(i+1, N):
            if salaries[i] > salaries[j]:
                expected_damages += salaries[i] - salaries[j]
    return expected_damages / N ** 2


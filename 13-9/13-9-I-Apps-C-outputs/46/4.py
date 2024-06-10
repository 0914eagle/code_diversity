
import math

def get_salaries(N, L, R):
    salaries = []
    for i in range(N):
        salaries.append(random.uniform(L[i], R[i]))
    return salaries

def get_damages(salaries):
    damages = 0
    for i in range(len(salaries)):
        for j in range(i+1, len(salaries)):
            if salaries[i] < salaries[j]:
                damages += salaries[j] - salaries[i]
    return damages

def get_expected_damages(N, L, R):
    salaries = get_salaries(N, L, R)
    damages = get_damages(salaries)
    return damages / N ** 2

if __name__ == '__main__':
    N = int(input())
    L = []
    R = []
    for i in range(N):
        l, r = map(float, input().split())
        L.append(l)
        R.append(r)
    print(get_expected_damages(N, L, R))


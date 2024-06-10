
import math

def get_salaries(n, low, high):
    return [random.uniform(low, high) for _ in range(n)]

def get_expected_damages(salaries):
    n = len(salaries)
    damages = 0
    for i in range(n):
        for j in range(i+1, n):
            if salaries[i] < salaries[j]:
                damages += salaries[j] - salaries[i]
    return damages / n ** 2

def main():
    n = int(input())
    low, high = map(float, input().split())
    salaries = get_salaries(n, low, high)
    print(get_expected_damages(salaries))

if __name__ == '__main__':
    main()


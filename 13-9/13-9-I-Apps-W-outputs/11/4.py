
def get_min_problems(c, d, n, m, k):
    total_winners = n*m + k
    min_problems = 0
    if total_winners % c == 0:
        min_problems = total_winners // c
    else:
        min_problems = total_winners // c + 1
    return min_problems

def get_min_additional_problems(d, n, m, k):
    total_winners = n*m + k
    min_problems = 0
    if total_winners % d == 0:
        min_problems = total_winners // d
    else:
        min_problems = total_winners // d + 1
    return min_problems

if __name__ == '__main__':
    c, d, n, m, k = map(int, input().split())
    min_problems = get_min_problems(c, d, n, m, k)
    min_additional_problems = get_min_additional_problems(d, n, m, k)
    print(min_problems + min_additional_problems)


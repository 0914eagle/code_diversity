
def get_maximum_score(n, t, a, t_i):
    # Write your code here
    return 0

def get_problems_to_solve(n, t, a, t_i):
    # Write your code here
    return []

if __name__ == '__main__':
    n, t = map(int, input().split())
    a = []
    t_i = []
    for i in range(n):
        a_i, t_i_i = map(int, input().split())
        a.append(a_i)
        t_i.append(t_i_i)
    maximum_score = get_maximum_score(n, t, a, t_i)
    problems_to_solve = get_problems_to_solve(n, t, a, t_i)
    print(maximum_score)
    print(len(problems_to_solve))
    print(*problems_to_solve)


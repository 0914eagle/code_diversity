
def f1(n, pegs, t, plan):
    # Function to check if the plan is safe and uses at most 10 times the number of pegs as the safe dry plan
    safe_plan = []
    for i in range(t):
        if plan[i] == 1:
            safe_plan.append(i)
        else:
            safe_plan.pop()
    if len(safe_plan) > 10 * len(pegs):
        return False
    return True

def f2(n, pegs, t, plan):
    # Function to find a safe wet plan using at most 10 times the number of pegs as the safe dry plan
    safe_plan = []
    for i in range(t):
        if plan[i] == 1:
            safe_plan.append(i)
        else:
            safe_plan.pop()
    if len(safe_plan) > 10 * len(pegs):
        return [-1]
    return safe_plan

if __name__ == '__main__':
    n = int(input())
    pegs = []
    for i in range(n):
        pegs.append(int(input()))
    t = int(input())
    plan = []
    for i in range(t):
        plan.append(int(input()))
    safe_plan = f2(n, pegs, t, plan)
    if safe_plan == [-1]:
        print(-1)
    else:
        print(len(safe_plan))
        for i in safe_plan:
            print(i)


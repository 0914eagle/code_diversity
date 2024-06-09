
def f1(n, pegs, t, plan):
    # Function to check if the plan is safe
    def is_safe(plan):
        for i in range(1, n + 1):
            if plan[i] == 1 and not any(plan[j] == 1 for j in pegs[i]):
                return False
        return True

    # Function to update the plan
    def update_plan(plan):
        for i in range(1, n + 1):
            if plan[i] == 1 and not any(plan[j] == 1 for j in pegs[i]):
                plan[i] = 0
        return plan

    # Initialize the plan
    plan = [0] * (n + 1)
    for i in range(t):
        plan[plan[i]] = 1

    # Check if the plan is safe
    if is_safe(plan):
        return plan

    # Update the plan
    plan = update_plan(plan)

    # Check if the updated plan is safe
    if is_safe(plan):
        return plan

    # If no safe plan can be found, return -1
    return -1

def f2(n, pegs, t, plan):
    # Function to check if the plan is safe
    def is_safe(plan):
        for i in range(1, n + 1):
            if plan[i] == 1 and not any(plan[j] == 1 for j in pegs[i]):
                return False
        return True

    # Function to update the plan
    def update_plan(plan):
        for i in range(1, n + 1):
            if plan[i] == 1 and not any(plan[j] == 1 for j in pegs[i]):
                plan[i] = 0
        return plan

    # Initialize the plan
    plan = [0] * (n + 1)
    for i in range(t):
        plan[plan[i]] = 1

    # Check if the plan is safe
    if is_safe(plan):
        return plan

    # Update the plan
    plan = update_plan(plan)

    # Check if the updated plan is safe
    if is_safe(plan):
        return plan

    # If no safe plan can be found, return -1
    return -1

if __name__ == '__main__':
    n = int(input())
    pegs = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        pegs[i] = list(map(int, input().split()))
    t = int(input())
    plan = [int(input()) for _ in range(t)]
    print(f1(n, pegs, t, plan))
    print(f2(n, pegs, t, plan))


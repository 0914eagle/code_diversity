
def f1(n, m, pegs):
    # Initialize a list to store the pegs
    peg_list = []
    # Iterate through the pegs and add them to the list
    for i in range(n):
        for j in range(m):
            if pegs[i][j] == 1:
                peg_list.append(i+1)
    return peg_list

def f2(n, m, pegs, plan):
    # Initialize a list to store the safe wet plan
    safe_wet_plan = []
    # Iterate through the plan and add the pegs to the list
    for i in range(n):
        if plan[i] == 1:
            safe_wet_plan.append(pegs[i])
    return safe_wet_plan

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    pegs = []
    for i in range(n):
        pegs.append(list(map(int, input().split())))
    plan = list(map(int, input().split()))
    peg_list = f1(n, m, pegs)
    safe_wet_plan = f2(n, m, pegs, plan)
    print(safe_wet_plan)


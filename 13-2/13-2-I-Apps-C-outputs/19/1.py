
def f1(n, pegs, t, plan):
    # Your code here
    return plan

def f2(n, pegs, t, plan):
    # Your code here
    return plan

if __name__ == '__main__':
    n = int(input())
    pegs = []
    for i in range(n):
        pegs.append(list(map(int, input().split())))
    t = int(input())
    plan = []
    for i in range(t):
        plan.append(int(input()))
    print(f1(n, pegs, t, plan))
    print(f2(n, pegs, t, plan))


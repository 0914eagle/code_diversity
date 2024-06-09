
def f1(n, m, pegs, dry_plan, wet_plan):
    # Your code here
    return dry_plan

def f2(n, m, pegs, dry_plan, wet_plan):
    # Your code here
    return wet_plan

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    pegs = []
    for i in range(n):
        pegs.append(set(map(int, input().split())))
    dry_plan = []
    for i in range(m):
        dry_plan.append(int(input()))
    wet_plan = []
    for i in range(m):
        wet_plan.append(int(input()))
    print(f1(n, m, pegs, dry_plan, wet_plan))
    print(f2(n, m, pegs, dry_plan, wet_plan))


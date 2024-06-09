
def f1(n, pegs, dry_plan, wet_plan):
    # Your code here
    return dry_plan

def f2(n, pegs, dry_plan, wet_plan):
    # Your code here
    return wet_plan

if __name__ == '__main__':
    n = int(input())
    pegs = []
    for i in range(n):
        pegs.append(list(map(int, input().split())))
    dry_plan = list(map(int, input().split()))
    wet_plan = list(map(int, input().split()))
    print(f1(n, pegs, dry_plan, wet_plan))
    print(f2(n, pegs, dry_plan, wet_plan))


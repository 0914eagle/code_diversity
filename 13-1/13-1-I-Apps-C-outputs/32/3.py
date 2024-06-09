
def is_valid_configuration(targets):
    # Check if the targets are valid
    for i in range(len(targets)):
        if targets[i][0] == targets[i][1]:
            return False
    
    # Check if there are no more than two targets in each row and column
    rows = [[] for _ in range(n)]
    cols = [[] for _ in range(n)]
    for target in targets:
        rows[target[0] - 1].append(target[1])
        cols[target[1] - 1].append(target[0])
    
    for row in rows:
        if len(row) > 2:
            return False
    for col in cols:
        if len(col) > 2:
            return False
    
    return True

def construct_targets(hits):
    targets = []
    for i in range(n):
        for j in range(i + 1, n):
            if hits[i] > 0 and hits[j] > 0:
                targets.append([i + 1, j + 1])
                hits[i] -= 1
                hits[j] -= 1
    
    for i in range(n):
        if hits[i] > 0:
            targets.append([i + 1, n])
    
    return targets

def solve():
    n = int(input())
    hits = list(map(int, input().split()))
    
    targets = construct_targets(hits)
    if is_valid_configuration(targets):
        print(len(targets))
        for target in targets:
            print(" ".join(map(str, target)))
    else:
        print(-1)

solve()


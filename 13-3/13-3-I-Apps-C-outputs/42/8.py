
def solve(N):
    nodes = [i for i in range(1, 2**N)]
    root = nodes[0]
    result = [root]
    for i in range(1, N):
        left = nodes[2**i-1:2**(i+1)-1]
        right = nodes[2**(i+1)-1:]
        result += left + right
    return " ".join(map(str, result))



def get_cost(c):
    return c[0] + c[1] + c[2] + c[3] + c[4] + c[5] + c[6] + c[7] + c[8]

def get_min_cost(costs, digits):
    min_cost = 0
    for i in range(len(digits)):
        for j in range(i+1, len(digits)):
            if digits[i] != -1 and digits[j] != -1:
                min_cost += costs[digits[i]][digits[j]]
    return min_cost

def solve(H, W, costs, digits):
    min_cost = get_min_cost(costs, digits)
    for i in range(H):
        for j in range(W):
            if digits[i*W+j] != -1:
                for k in range(10):
                    if k != digits[i*W+j]:
                        digits[i*W+j] = k
                        min_cost = min(min_cost, get_min_cost(costs, digits))
                        digits[i*W+j] = digits[i*W+j]
    return min_cost

if __name__ == '__main__':
    H, W = map(int, input().split())
    costs = []
    for i in range(10):
        costs.append(list(map(int, input().split())))
    digits = []
    for i in range(H*W):
        digits.append(int(input()))
    print(solve(H, W, costs, digits))


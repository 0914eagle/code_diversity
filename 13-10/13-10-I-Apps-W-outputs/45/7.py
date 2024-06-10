
def get_total_instability(weights, n):
    total_instability = 0
    for i in range(n):
        for j in range(i+1, n):
            total_instability += abs(weights[i] - weights[j])
    return total_instability

def solve(weights):
    n = len(weights) // 2
    total_instability = get_total_instability(weights, n)
    for i in range(n):
        for j in range(i+1, n):
            weights[i], weights[j] = weights[j], weights[i]
            new_total_instability = get_total_instability(weights, n)
            if new_total_instability < total_instability:
                total_instability = new_total_instability
                break
        weights[i], weights[j] = weights[j], weights[i]
    return total_instability

if __name__ == '__main__':
    n = int(input())
    weights = list(map(int, input().split()))
    print(solve(weights))



def get_tandem_instability(weights):
    instability = 0
    for i in range(0, len(weights), 2):
        instability += abs(weights[i] - weights[i+1])
    return instability

def get_single_instability(weights):
    instability = 0
    for i in range(len(weights)):
        instability += weights[i]
    return instability

def get_min_total_instability(weights):
    tandem_instability = get_tandem_instability(weights)
    single_instability = get_single_instability(weights)
    return min(tandem_instability, single_instability)

if __name__ == '__main__':
    n = int(input())
    weights = list(map(int, input().split()))
    print(get_min_total_instability(weights))


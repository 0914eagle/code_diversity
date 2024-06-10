
def get_total_instability(weights):
    # Initialize variables
    total_instability = 0
    tandem_kayaks = []
    single_kayaks = []

    # Sort the weights in descending order
    weights.sort(reverse=True)

    # Iterate through the weights and assign them to kayaks
    for i in range(len(weights)):
        if i % 2 == 0:
            # Even index means it's a tandem kayak
            tandem_kayaks.append(weights[i])
        else:
            # Odd index means it's a single kayak
            single_kayaks.append(weights[i])

    # Calculate the instability of each kayak
    for kayak in tandem_kayaks:
        total_instability += abs(kayak[0] - kayak[1])

    # Calculate the instability of the single kayaks
    for kayak in single_kayaks:
        total_instability += kayak

    return total_instability

def solve(n, weights):
    # Initialize variables
    min_total_instability = float('inf')
    assignment = []

    # Generate all possible assignments of weights to kayaks
    for i in range(len(weights)):
        for j in range(i+1, len(weights)):
            assignment.append((weights[i], weights[j]))

    # Iterate through the assignments and calculate the total instability
    for tandem_kayak in assignment:
        total_instability = get_total_instability(tandem_kayak)
        if total_instability < min_total_instability:
            min_total_instability = total_instability

    return min_total_instability

if __name__ == '__main__':
    n = int(input())
    weights = list(map(int, input().split()))
    print(solve(n, weights))


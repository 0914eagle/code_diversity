
def get_maximum_tastiness_per_coin(n, k, a, b, tastiness, additional_tastiness):
    # Initialize the optimal solution
    opt = 0

    # Loop through all possible combinations of scoops
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                # Calculate the total tastiness and cost of the current combination
                total_tastiness = tastiness[i - 1] + tastiness[j - 1] + tastiness[k - 1]
                total_cost = a * i + b + a * j + b + a * k + b

                # Calculate the tastiness per coin ratio
                tastiness_per_coin = total_tastiness / total_cost

                # Update the optimal solution if the current combination is better
                if tastiness_per_coin > opt:
                    opt = tastiness_per_coin

    return opt

def main():
    # Read the input
    n, k, a, b = map(int, input().split())
    tastiness = list(map(int, input().split()))
    additional_tastiness = []
    for i in range(k):
        additional_tastiness.append(list(map(int, input().split())))

    # Calculate the maximum tastiness per coin ratio
    opt = get_maximum_tastiness_per_coin(n, k, a, b, tastiness, additional_tastiness)

    # Print the result
    print(opt)

if __name__ == '__main__':
    main()


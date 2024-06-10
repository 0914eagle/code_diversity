customers_served(N, M, P, R, customers):
    customers.sort(key=lambda x: x[1])  # Sort customers by arrival time
    wearing = set()  # Set to keep track of clothing types Fluttershy is wearing
    max_customers = 0

    for customer in customers:
        clothing_type, arrival_time = customer
        if clothing_type not in wearing:
            time_to_change = max([P[i - 1] for i in wearing], default=0)  # Time to change clothing
            if time_to_change <= arrival_time:
                wearing.add(clothing_type)
                wearing.difference_update([i for i in wearing if R[i - 1] <= arrival_time - time_to_change])
                max_customers += 1

    return max_customers

if __name__ == "__main__":
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    R = list(map(int, input().split()))
    customers = [list(map(int, input().split())) for _ in range(N)]

    result = max_customers_served(N, M, P, R, customers)
    print(result)

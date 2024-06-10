customers_served(N, M, P, R, customers):
    customers.sort(key=lambda x: x[1])  # Sort customers by arrival time
    wearing = set()  # Set to keep track of clothing types Fluttershy is wearing
    served = 0  # Counter for the number of customers served

    for customer in customers:
        clothing_type, arrival_time = customer
        if clothing_type not in wearing:
            time_to_change = P[clothing_type - 1]  # Time needed to change into required clothing
            if arrival_time >= time_to_change:
                wearing.add(clothing_type)
                served += 1

    return served

if __name__ == "__main__":
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    R = list(map(int, input().split()))
    customers = [list(map(int, input().split())) for _ in range(N)]

    result = max_customers_served(N, M, P, R, customers)
    print(result)

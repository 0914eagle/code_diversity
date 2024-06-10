mum_customers_served(N, M, P, R, customers):
    customers.sort(key=lambda x: x[1])  # Sort customers by arrival time
    clothing_types = set()
    max_customers_served = 0

    for customer in customers:
        clothing_type, arrival_time = customer
        if clothing_type not in clothing_types:
            time_to_change = P[clothing_type - 1] if not clothing_types else max(P[i - 1] for i in clothing_types)
            if arrival_time >= time_to_change:
                clothing_types.add(clothing_type)
                max_customers_served += 1

    return max_customers_served


if __name__ == "__main__":
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    R = list(map(int, input().split()))
    customers = [list(map(int, input().split())) for _ in range(N)]

    result = maximum_customers_served(N, M, P, R, customers)
    print(result)

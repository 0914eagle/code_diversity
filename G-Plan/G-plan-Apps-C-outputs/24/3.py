mum_customers_served(N, M, clothing_put_on, clothing_remove, customers):
    customers.sort(key=lambda x: x[1])  # Sort customers by arrival time
    wearing_clothing = set()
    max_customers_served = 0

    for customer in customers:
        clothing_type, arrival_time = customer
        if clothing_type not in wearing_clothing:
            time_to_change = clothing_put_on[clothing_type - 1]
            if arrival_time >= time_to_change:
                wearing_clothing.add(clothing_type)
                max_customers_served += 1

    return max_customers_served


if __name__ == "__main__":
    N, M = map(int, input().split())
    clothing_put_on = list(map(int, input().split()))
    clothing_remove = list(map(int, input().split()))
    customers = [list(map(int, input().split())) for _ in range(N)]

    result = maximum_customers_served(N, M, clothing_put_on, clothing_remove, customers)
    print(result)

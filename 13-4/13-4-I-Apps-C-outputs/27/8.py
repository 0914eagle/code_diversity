
import math

def get_delivery_time(customers, company):
    
    delivery_time = 0
    for i in range(len(customers)):
        current_customer = customers[i]
        next_customer = customers[(i + 1) % len(customers)]
        delivery_time += math.ceil(math.sqrt((next_customer[0] - current_customer[0]) ** 2 + (next_customer[1] - current_customer[1]) ** 2))
    return delivery_time

def get_longest_delivery_time(customers):
    
    company_a_customers = customers[:len(customers) // 2]
    company_b_customers = customers[len(customers) // 2:]
    delivery_time_a = get_delivery_time(company_a_customers, "A")
    delivery_time_b = get_delivery_time(company_b_customers, "B")
    return max(delivery_time_a, delivery_time_b)

def main():
    num_customers = int(input())
    customers = []
    for _ in range(num_customers):
        x, y = map(int, input().split())
        customers.append((x, y))
    print(get_longest_delivery_time(customers))

if __name__ == '__main__':
    main()


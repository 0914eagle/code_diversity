
def f1(customers):
    # Your code here
    return longest_delivery_time

def f2(customers):
    # Your code here
    return longest_delivery_time

if __name__ == '__main__':
    num_customers = int(input())
    customers = []
    for _ in range(num_customers):
        x, y = map(int, input().split())
        customers.append((x, y))

    longest_delivery_time = max(f1(customers), f2(customers))
    print(longest_delivery_time)



def f1(customers):
    # your code here
    return ...

def f2(customers):
    # your code here
    return ...

if __name__ == '__main__':
    num_customers = int(input())
    customers = []
    for _ in range(num_customers):
        x, y = map(int, input().split())
        customers.append((x, y))

    print(max(f1(customers), f2(customers)))


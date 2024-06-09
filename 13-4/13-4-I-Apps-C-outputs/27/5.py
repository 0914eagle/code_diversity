
def f1(customers):
    # f1 should return the longest delivery time required by the first company
    return 0

def f2(customers):
    # f2 should return the longest delivery time required by the second company
    return 0

if __name__ == '__main__':
    num_customers = int(input())
    customers = []
    for i in range(num_customers):
        x, y = map(int, input().split())
        customers.append((x, y))
    print(max(f1(customers), f2(customers)))


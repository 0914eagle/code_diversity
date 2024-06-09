
def f1(N, customers):
    # Your code here
    return longest_delivery_time

def f2(N, customers):
    # Your code here
    return longest_delivery_time

if __name__ == '__main__':
    N = int(input())
    customers = []
    for i in range(N):
        x, y = map(int, input().split())
        customers.append((x, y))

    print(f1(N, customers))
    print(f2(N, customers))


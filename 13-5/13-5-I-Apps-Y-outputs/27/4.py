
def f1(n, a):
    # Calculate the number of possible orders
    num_orders = 1
    for i in range(n):
        num_orders *= len(a) - a[i]
    
    # Calculate the modulo 10^9+7
    num_orders %= 1000000007
    
    return num_orders

def f2(n, a):
    # Initialize the possible orders
    orders = []
    
    # Generate all possible orders
    for i in range(n):
        for j in range(len(a)):
            if j not in orders:
                orders.append(j)
    
    # Calculate the number of possible orders
    num_orders = len(orders)
    
    return num_orders

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    
    print(f1(n, a))
    print(f2(n, a))



def f1(n, a):
    # Calculate the number of possible orders
    num_orders = 1
    for i in range(n):
        num_orders *= len(a) - a[i]
    
    # Calculate the modulo 10^9+7
    num_orders %= 1000000007
    
    return num_orders


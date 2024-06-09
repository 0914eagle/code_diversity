
def f1(n, a):
    # Calculate the number of possible orders
    num_orders = 1
    for i in range(n):
        num_orders *= (n - i)
    
    # Calculate the number of incorrect orders
    num_incorrect = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j]:
                num_incorrect += 1
    
    # Return the number of possible orders minus the number of incorrect orders
    return num_orders - num_incorrect

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))


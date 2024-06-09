
def f1(n, p):
    # Calculate the total number of apples sold
    total_apples = n * p // 2
    
    # Calculate the total money earned
    total_money = total_apples * p
    
    return total_money

def f2(n, p):
    # Calculate the total number of apples sold
    total_apples = n * p // 2
    
    # Calculate the total money earned
    total_money = total_apples * p
    
    return total_money

if __name__ == '__main__':
    n, p = map(int, input().split())
    print(f1(n, p))


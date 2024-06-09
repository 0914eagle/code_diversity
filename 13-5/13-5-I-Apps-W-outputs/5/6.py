
def f1(n, p):
    # Calculate the total number of apples sold
    total_apples = n * (p / 2)
    
    # Calculate the total cost of the apples
    total_cost = total_apples * p
    
    return total_cost

def f2(n, p):
    # Calculate the total number of apples sold
    total_apples = n * (p / 2)
    
    # Calculate the total cost of the apples
    total_cost = total_apples * p
    
    # Calculate the total money grandma should have at the end of the day
    total_money = total_cost - (total_apples / 2)
    
    return total_money

if __name__ == '__main__':
    n = int(input())
    p = int(input())
    print(f2(n, p))


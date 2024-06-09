
def f1(jacketCost, sockCost, money):
    # Calculate the number of socks that Chef can buy
    num_socks = money // sockCost
    
    # Calculate the number of days until Chef has only 1 clean sock
    days = num_socks // 2
    
    # If the number of days is odd, Chef will have only 1 clean sock on the last day
    if days % 2 == 1:
        return "Unlucky Chef"
    else:
        return "Lucky Chef"

def f2(jacketCost, sockCost, money):
    # Calculate the number of socks that Chef can buy
    num_socks = money // sockCost
    
    # Calculate the number of days until Chef has only 1 clean sock
    days = num_socks // 2
    
    # If the number of days is odd, Chef will have only 1 clean sock on the last day
    if days % 2 == 1:
        return "Unlucky Chef"
    else:
        return "Lucky Chef"

if __name__ == '__main__':
    jacketCost, sockCost, money = map(int, input().split())
    print(f1(jacketCost, sockCost, money))
    print(f2(jacketCost, sockCost, money))



def f1(jacket_cost, sock_cost, money):
    # Calculate the number of socks Chef can buy
    num_socks = money // sock_cost
    
    # Calculate the number of days Chef can use socks
    num_days = num_socks // 2
    
    # Check if there will be a day when Chef has only 1 clean sock
    if num_days % 2 == 1:
        return "Unlucky Chef"
    else:
        return "Lucky Chef"

def f2(jacket_cost, sock_cost, money):
    # Calculate the number of socks Chef can buy
    num_socks = money // sock_cost
    
    # Calculate the number of days Chef can use socks
    num_days = num_socks // 2
    
    # Check if there will be a day when Chef has only 1 clean sock
    if num_days % 2 == 1:
        return "Unlucky Chef"
    else:
        return "Lucky Chef"

if __name__ == '__main__':
    jacket_cost, sock_cost, money = map(int, input().split())
    print(f1(jacket_cost, sock_cost, money))


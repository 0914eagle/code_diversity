
def f1(jacket_cost, sock_cost, money):
    # Calculate the number of socks Chef can buy
    num_socks = money // sock_cost
    
    # Calculate the number of pairs of socks Chef can buy
    num_pairs = num_socks // 2
    
    # Calculate the number of days Chef can use socks
    num_days = num_pairs + 1
    
    # Check if there is a day when Chef will have only 1 clean sock
    if num_days % 2 == 1:
        return "Unlucky Chef"
    else:
        return "Lucky Chef"

def f2(jacket_cost, sock_cost, money):
    # Calculate the number of socks Chef can buy
    num_socks = money // sock_cost
    
    # Calculate the number of pairs of socks Chef can buy
    num_pairs = num_socks // 2
    
    # Calculate the number of days Chef can use socks
    num_days = num_pairs + 1
    
    # Check if there is a day when Chef will have only 1 clean sock
    if num_days % 2 == 1:
        return "Unlucky Chef"
    else:
        return "Lucky Chef"

if __name__ == '__main__':
    jacket_cost = int(input())
    sock_cost = int(input())
    money = int(input())
    print(f1(jacket_cost, sock_cost, money))
    print(f2(jacket_cost, sock_cost, money))


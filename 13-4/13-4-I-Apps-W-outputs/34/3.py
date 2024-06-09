
def f1(jacket_cost, sock_cost, money):
    # Calculate the number of socks Chef can buy
    num_socks = money // sock_cost
    
    # Calculate the number of days Chef will have only 1 clean sock
    days = num_socks // 2
    
    # If there is a day when Chef will have only 1 clean sock, return "Unlucky Chef"
    if days > 0:
        return "Unlucky Chef"
    
    # Otherwise, return "Lucky Chef"
    return "Lucky Chef"

def f2(jacket_cost, sock_cost, money):
    # Calculate the number of socks Chef can buy
    num_socks = money // sock_cost
    
    # Calculate the number of days Chef will have only 1 clean sock
    days = num_socks // 2
    
    # If there is a day when Chef will have only 1 clean sock, return "Unlucky Chef"
    if days > 0:
        return "Unlucky Chef"
    
    # Otherwise, return "Lucky Chef"
    return "Lucky Chef"

if __name__ == '__main__':
    jacket_cost = int(input())
    sock_cost = int(input())
    money = int(input())
    print(f1(jacket_cost, sock_cost, money))
    print(f2(jacket_cost, sock_cost, money))


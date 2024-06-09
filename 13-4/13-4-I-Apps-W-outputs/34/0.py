
def get_unlucky_day(jacket_cost, sock_cost, money):
    # Calculate the number of socks that Chef can buy with the given money
    num_socks = money // sock_cost
    
    # Calculate the number of days it takes for Chef to use all the socks he has bought
    num_days = num_socks // 2
    
    # Check if there is a day when Chef will have only 1 clean sock left
    if num_days % 2 == 1:
        return "Unlucky Chef"
    else:
        return "Lucky Chef"
    
def main():
    jacket_cost, sock_cost, money = map(int, input().split())
    print(get_unlucky_day(jacket_cost, sock_cost, money))
    
if __name__ == '__main__':
    main()


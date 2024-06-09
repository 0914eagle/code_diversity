
def calculate_interest(balance, interest_rate):
    return balance * (1 + interest_rate)

def calculate_years_to_reach_x(balance, interest_rate, x):
    years = 0
    while balance < x:
        balance = calculate_interest(balance, interest_rate)
        years += 1
    return years

if __name__ == '__main__':
    x = int(input())
    balance = 100
    interest_rate = 0.01
    years = calculate_years_to_reach_x(balance, interest_rate, x)
    print(years)


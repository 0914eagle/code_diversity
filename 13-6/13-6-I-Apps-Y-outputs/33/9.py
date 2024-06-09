
def calculate_interest(balance, interest_rate):
    return balance * (1 + interest_rate)

def find_years_to_reach_balance(initial_balance, target_balance, interest_rate):
    years = 0
    balance = initial_balance
    while balance < target_balance:
        balance = calculate_interest(balance, interest_rate)
        years += 1
    return years

if __name__ == '__main__':
    target_balance = int(input())
    interest_rate = 0.01
    initial_balance = 100
    years = find_years_to_reach_balance(initial_balance, target_balance, interest_rate)
    print(years)


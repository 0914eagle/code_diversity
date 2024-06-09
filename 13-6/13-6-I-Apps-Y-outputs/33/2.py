
def calculate_interest(balance, interest_rate):
    return balance * (1 + interest_rate)

def solve(x):
    balance = 100
    years = 0
    while balance < x:
        balance = calculate_interest(balance, 0.01)
        years += 1
    return years

if __name__ == '__main__':
    x = int(input())
    print(solve(x))



def get_average_cost(shares_bought, shares_sold, cost):
    return (shares_bought - shares_sold) * cost / shares_bought

def get_final_sale_price(shares_sold, cost, tax_rate):
    return shares_sold * cost * (1 - tax_rate)

def get_tax_amount(shares_sold, cost, tax_rate):
    return shares_sold * cost * tax_rate

def get_profit(shares_sold, cost, tax_rate):
    return get_final_sale_price(shares_sold, cost, tax_rate) - get_tax_amount(shares_sold, cost, tax_rate)

def solve(events):
    shares_bought = 0
    shares_sold = 0
    cost = 0
    tax_rate = 0.3
    for event in events:
        if event.startswith("buy"):
            shares_bought += int(event.split()[1])
            cost += int(event.split()[2]) * int(event.split()[1])
        elif event.startswith("sell"):
            shares_sold += int(event.split()[1])
            cost -= int(event.split()[2]) * int(event.split()[1])
        elif event.startswith("split"):
            shares_bought *= int(event.split()[1])
            cost /= int(event.split()[1])
        elif event.startswith("merge"):
            shares_sold += int(event.split()[1]) - 1
            cost = get_average_cost(shares_bought, shares_sold, cost)
        elif event.startswith("die"):
            return get_profit(shares_sold, cost, tax_rate)
    return 0

if __name__ == '__main__':
    events = []
    while True:
        try:
            events.append(input())
        except EOFError:
            break
    print(solve(events))


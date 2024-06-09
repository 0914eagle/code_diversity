
def get_cost(shares, cost):
    return shares * cost

def get_average_cost(shares, cost):
    return cost

def get_profit(shares, cost, sell_price):
    return (sell_price - cost) * shares

def get_tax(profit, tax_rate):
    return profit * tax_rate

def get_net_profit(profit, tax):
    return profit - tax

def get_final_sale_price(shares, cost, sell_price, tax_rate):
    profit = get_profit(shares, cost, sell_price)
    tax = get_tax(profit, tax_rate)
    net_profit = get_net_profit(profit, tax)
    return net_profit

def main():
    shares = 10
    cost = 10
    sell_price = 42
    tax_rate = 0.3
    final_sale_price = get_final_sale_price(shares, cost, sell_price, tax_rate)
    print(final_sale_price)

if __name__ == '__main__':
    main()



def get_average_cost(shares, cost):
    return sum(shares) * cost / len(shares)

def get_profit(sell_price, cost):
    return sell_price - cost

def get_tax(profit, tax_rate):
    return profit * tax_rate

def get_net_profit(profit, tax):
    return profit - tax

def split_shares(shares, num_new_shares):
    return [shares[i] / num_new_shares for i in range(num_new_shares)]

def merge_shares(shares, num_shares_to_merge):
    return [sum(shares[i:i+num_shares_to_merge]) for i in range(0, len(shares), num_shares_to_merge)]

def get_final_sale_profit(shares, cost, sell_price):
    profit = get_profit(sell_price, cost)
    tax = get_tax(profit, 0.3)
    net_profit = get_net_profit(profit, tax)
    return net_profit

def main():
    events = input().split()
    shares = []
    cost = 0
    for event in events:
        if event.startswith("buy"):
            num_shares, share_price = map(int, event.split(" ")[1:])
            shares.extend([share_price] * num_shares)
            cost += num_shares * share_price
        elif event.startswith("sell"):
            num_shares, sell_price = map(int, event.split(" ")[1:])
            profit = get_profit(sell_price, cost)
            tax = get_tax(profit, 0.3)
            net_profit = get_net_profit(profit, tax)
            cost -= net_profit
        elif event.startswith("split"):
            num_new_shares = int(event.split(" ")[1])
            shares = split_shares(shares, num_new_shares)
        elif event.startswith("merge"):
            num_shares_to_merge = int(event.split(" ")[1])
            shares = merge_shares(shares, num_shares_to_merge)
        elif event.startswith("die"):
            sell_price = int(event.split(" ")[1])
            final_sale_profit = get_final_sale_profit(shares, cost, sell_price)
            print(final_sale_profit)
            break

if __name__ == '__main__':
    main()



def get_average_cost(shares, cost):
    return sum(cost) / len(shares)

def get_profit(shares, cost, sale_price):
    return sum(sale_price) - sum(cost)

def get_tax(profit, tax_rate):
    return profit * tax_rate

def get_sale_price_after_tax(profit, tax):
    return profit - tax

def get_final_sale_price(shares, cost, sale_price, tax_rate):
    average_cost = get_average_cost(shares, cost)
    profit = get_profit(shares, cost, sale_price)
    tax = get_tax(profit, tax_rate)
    sale_price_after_tax = get_sale_price_after_tax(profit, tax)
    return sale_price_after_tax

def main():
    shares = []
    cost = []
    sale_price = []
    tax_rate = 0.3
    for line in sys.stdin:
        event = line.strip().split()
        if event[0] == "buy":
            shares.append(int(event[1]))
            cost.append(int(event[2]))
        elif event[0] == "sell":
            shares.pop()
            cost.pop()
            sale_price.append(int(event[2]))
        elif event[0] == "split":
            num_shares = int(event[1])
            for i in range(len(shares)):
                shares.extend([shares[i] for _ in range(num_shares)])
                cost.extend([cost[i] for _ in range(num_shares)])
        elif event[0] == "merge":
            num_shares = int(event[1])
            for i in range(len(shares) // num_shares):
                total_cost = sum(cost[i * num_shares:(i + 1) * num_shares])
                shares.pop()
                cost.pop()
                shares.append(num_shares)
                cost.append(total_cost / num_shares)
        elif event[0] == "die":
            sale_price.append(int(event[1]))
            break
    final_sale_price = get_final_sale_price(shares, cost, sale_price, tax_rate)
    print(final_sale_price)

if __name__ == '__main__':
    main()


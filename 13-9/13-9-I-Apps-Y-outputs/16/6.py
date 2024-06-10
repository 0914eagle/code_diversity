
def compute_tax(profit, tax_rate):
    return profit - (profit * tax_rate)

def compute_average_cost(costs, shares):
    return sum(costs) / len(costs)

def compute_profit(sell_price, average_cost):
    return sell_price - average_cost

def split_stock(shares, x):
    return shares * x

def merge_stock(shares, x):
    return int(shares / x)

def sell_stock(shares, sell_price):
    return shares * sell_price

def main():
    events = input().split()
    costs = []
    shares = 0
    average_cost = 0
    for event in events:
        action, x, y = event.split(" ")
        x = int(x)
        y = int(y)
        if action == "buy":
            costs.extend([y] * x)
            shares += x
            average_cost = compute_average_cost(costs, shares)
        elif action == "sell":
            average_cost = compute_average_cost(costs, shares)
            profit = compute_profit(y, average_cost)
            tax = compute_tax(profit, 0.3)
            print(f"Profit: {profit:.6f} Tax: {tax:.6f}")
            shares -= x
            costs = costs[:shares]
        elif action == "split":
            shares = split_stock(shares, x)
        elif action == "merge":
            shares = merge_stock(shares, x)
        elif action == "die":
            sell_price = y
            average_cost = compute_average_cost(costs, shares)
            profit = compute_profit(sell_price, average_cost)
            tax = compute_tax(profit, 0.3)
            print(f"Profit: {profit:.6f} Tax: {tax:.6f}")
            break
    return shares, costs, average_cost

if __name__ == "__main__":
    main()


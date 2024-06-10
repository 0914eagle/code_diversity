
import math

def get_average_cost(costs, shares):
    return sum(costs) / len(costs)

def get_profit(costs, shares, sale_price):
    return sale_price - get_average_cost(costs, shares)

def get_tax(profit, tax_rate):
    return profit * tax_rate

def get_net_profit(profit, tax):
    return profit - tax

def solve(events):
    costs = []
    shares = 0
    for event in events:
        if event[0] == "buy":
            costs.append(event[2])
            shares += event[1]
        elif event[0] == "sell":
            costs.append(event[2])
            shares -= event[1]
        elif event[0] == "split":
            new_shares = event[1] * shares
            costs = [cost / event[1] for cost in costs]
            shares = new_shares
        elif event[0] == "merge":
            new_shares = shares // event[1]
            costs = [math.floor(cost * event[1]) for cost in costs]
            shares = new_shares
        elif event[0] == "die":
            profit = get_profit(costs, shares, event[1])
            tax = get_tax(profit, 0.3)
            net_profit = get_net_profit(profit, tax)
            return net_profit
    return 0.0

def main():
    events = []
    for line in sys.stdin:
        event = line.strip().split()
        events.append(event)
    print(solve(events))

if __name__ == '__main__':
    main()



def get_cost(shares, cost):
    return sum(shares) * cost

def get_average_cost(shares, cost):
    return sum(shares) * cost / len(shares)

def get_profit(shares, cost, sale_price):
    return (sale_price - cost) * len(shares)

def get_tax(profit, tax_rate):
    return profit * tax_rate

def get_net_profit(profit, tax):
    return profit - tax

def f1(events):
    shares = []
    cost = 0
    for event in events:
        if event[0] == "buy":
            shares.append(event[1])
            cost += event[2] * event[1]
        elif event[0] == "sell":
            cost -= event[2] * event[1]
        elif event[0] == "split":
            for i in range(event[1]):
                shares.append(1)
        elif event[0] == "merge":
            for i in range(len(shares) // event[1]):
                shares[i * event[1]] += event[1] - 1
                shares = shares[1:]
        elif event[0] == "die":
            break
    return get_net_profit(get_profit(shares, cost, event[1]), get_tax(get_profit(shares, cost, event[1]), 0.3))

def f2(...):
    ...

if __name__ == '__main__':
    events = [
        ["buy", 10, 10],
        ["buy", 30, 5],
        ["sell", 31, 8],
        ["split", 2],
        ["merge", 8],
        ["die", 42]
    ]
    print(f1(events))



def get_share_value(shares, cost):
    return cost / shares

def get_average_cost(shares, cost):
    return cost / shares

def get_split_value(shares, cost, x):
    return cost / shares * x

def get_merge_value(shares, cost, x):
    return cost / shares * x

def get_sale_value(shares, cost, x):
    return cost / shares * x

def get_tax_value(value, tax_rate):
    return value * tax_rate

def get_final_value(value, tax_value):
    return value - tax_value

def main():
    shares = 10
    cost = 10
    events = []
    while True:
        event = input()
        if event == "die":
            break
        elif event.startswith("buy"):
            shares += int(event.split()[1])
            cost += int(event.split()[2]) * int(event.split()[1])
        elif event.startswith("sell"):
            shares -= int(event.split()[1])
            cost -= int(event.split()[2]) * int(event.split()[1])
        elif event.startswith("split"):
            x = int(event.split()[1])
            shares *= x
            cost = get_split_value(shares, cost, x)
        elif event.startswith("merge"):
            x = int(event.split()[1])
            shares = shares // x
            cost = get_merge_value(shares, cost, x)
        events.append(event)
    tax_rate = 0.3
    value = get_sale_value(shares, cost, int(input()))
    tax_value = get_tax_value(value, tax_rate)
    final_value = get_final_value(value, tax_value)
    print(final_value)

if __name__ == '__main__':
    main()


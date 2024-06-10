shares(shares, cost, total_shares, total_cost):
    total_shares += shares
    total_cost += shares * cost
    return total_shares, total_cost

def sell_shares(shares, cost, total_shares, total_cost, total_profit):
    profit = shares * cost - total_cost / total_shares * shares
    total_profit += profit
    total_shares -= shares
    total_cost -= shares * (total_cost / total_shares)
    return total_shares, total_cost, total_profit

def split_shares(split_factor, total_shares, total_cost):
    total_shares *= split_factor
    total_cost /= split_factor
    return total_shares, total_cost

def merge_shares(merge_factor, total_shares, total_cost):
    total_shares //= merge_factor
    total_cost *= merge_factor
    return total_shares, total_cost

def die_and_sell(shares, cost, total_shares, total_cost, total_profit, sell_price):
    profit = shares * sell_price - total_cost / total_shares * shares
    total_profit += profit
    return total_profit

if __name__ == "__main__":
    events = int(input())
    total_shares = 0
    total_cost = 0
    total_profit = 0

    for _ in range(events):
        event = input().split()
        if event[0] == "buy":
            total_shares, total_cost = buy_shares(int(event[1]), int(event[2]), total_shares, total_cost)
        elif event[0] == "sell":
            total_shares, total_cost, total_profit = sell_shares(int(event[1]), int(event[2]), total_shares, total_cost, total_profit)
        elif event[0] == "split":
            total_shares, total_cost = split_shares(int(event[1]), total_shares, total_cost)
        elif event[0] == "merge":
            total_shares, total_cost = merge_shares(int(event[1]), total_shares, total_cost)
        elif event[0] == "die":
            total_profit = die_and_sell(total_shares, total_cost, total_shares, total_cost, total_profit, int(event[1]))

    print("{:.8f}".format(total_profit))

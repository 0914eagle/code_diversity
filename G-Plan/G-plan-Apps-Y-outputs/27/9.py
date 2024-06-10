shares(shares, cost, total_shares, total_cost):
    total_shares += shares
    total_cost += shares * cost
    return total_shares, total_cost

def sell_shares(shares, cost, total_shares, total_cost, total_profit):
    profit = shares * cost - total_cost / total_shares * shares
    total_profit += profit
    total_shares -= shares
    total_cost -= shares * cost
    return total_shares, total_cost, total_profit

def split_shares(split_ratio, total_shares, total_cost):
    total_shares *= split_ratio
    total_cost /= split_ratio
    return total_shares, total_cost

def merge_shares(merge_ratio, total_shares, total_cost):
    total_shares //= merge_ratio
    total_cost *= merge_ratio
    return total_shares, total_cost

def die_sell(shares, cost, total_shares, total_cost, total_profit, final_price):
    profit = shares * final_price - total_cost / total_shares * shares
    total_profit += profit
    return total_profit

if __name__ == "__main__":
    total_shares = 0
    total_cost = 0
    total_profit = 0

    while True:
        try:
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
                final_price = int(event[1])
                total_profit = die_sell(total_shares, total_cost, total_profit, final_price)
                break
        except EOFError:
            break

    print("{:.8f}".format(total_profit)
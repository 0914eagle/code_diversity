
def calculate_final_amount(events):
    total_shares = 0
    total_cost = 0
    total_profit = 0

    for event in events:
        if event[0] == 'buy':
            x, y = event[1], event[2]
            total_shares += x
            total_cost += x * y
        elif event[0] == 'sell':
            x, y = event[1], event[2]
            profit_per_share = y - (total_cost / total_shares)
            total_profit += x * profit_per_share
            total_shares -= x
            total_cost -= x * profit_per_share
        elif event[0] == 'split':
            x = event[1]
            total_shares *= x
        elif event[0] == 'merge':
            x = event[1]
            total_shares //= x
        elif event[0] == 'die':
            y = event[1]
            total_profit += total_shares * (y - (total_cost / total_shares) * 0.7)

    return total_profit


if __name__ == "__main__":
    n = int(input())
    events = []
    for _ in range(n):
        event = input().split()
        if len(event) == 3:
            events.append((event[0], int(event[1]), int(event[2]))
        else:
            events.append((event[0], int(event[1])))

    result = calculate_final_amount(events)
    print("{:.8f}".format(result))

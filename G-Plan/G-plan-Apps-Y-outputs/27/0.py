
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
            profit = y - total_cost / total_shares
            total_profit += x * profit
            total_shares -= x
            total_cost -= x * (total_cost / total_shares)
        elif event[0] == 'split':
            x = event[1]
            total_shares *= x
        elif event[0] == 'merge':
            x = event[1]
            total_shares //= x
            total_cost *= x
        elif event[0] == 'die':
            y = event[1]
            profit = y - total_cost / total_shares
            total_profit += total_shares * profit * 0.7

    return total_profit

if __name__ == "__main__":
    events = []
    while True:
        try:
            event = input().split()
            if event[0] == 'die':
                events.append((event[0], int(event[1])))
                break
            elif event[0] == 'split' or event[0] == 'merge':
                events.append((event[0], int(event[1])))
            else:
                events.append((event[0], int(event[1]), int(event[2])))
        except EOFError:
            break

    result = calculate_final_amount(events)
    print("{:.8f}".format(result))


def calculate_final_amount(events):
    shares = 0
    total_cost = 0
    total_profit = 0

    for event in events:
        if event[0] == 'buy':
            x, y = event[1], event[2]
            shares += x
            total_cost += x * y
        elif event[0] == 'sell':
            x, y = event[1], event[2]
            profit_per_share = y - (total_cost / shares)
            total_profit += x * profit_per_share
            shares -= x
            total_cost -= x * (total_cost / shares) if shares > 0 else 0
        elif event[0] == 'split':
            x = event[1]
            shares *= x
        elif event[0] == 'merge':
            x = event[1]
            shares //= x
            total_cost *= x
        elif event[0] == 'die':
            y = event[1]
            remaining_profit = y - (total_cost / shares)
            total_profit += shares * remaining_profit * 0.7  # 30% tax
            break

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

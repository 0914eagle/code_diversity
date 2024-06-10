
def calculate_final_amount(events):
    shares = 0
    total_cost = 0
    total_profit = 0

    for event in events:
        if event[0] == 'buy':
            shares += event[1]
            total_cost += event[1] * event[2]
        elif event[0] == 'sell':
            profit_per_share = event[2] - total_cost / shares
            total_profit += event[1] * profit_per_share
            shares -= event[1]
            total_cost -= event[1] * total_cost / shares
        elif event[0] == 'split':
            shares *= event[1]
        elif event[0] == 'merge':
            shares //= event[1]
            total_cost *= event[1]
        elif event[0] == 'die':
            total_profit += shares * (event[1] - total_cost / shares * 0.3)
    
    return total_profit

if __name__ == "__main__":
    events = []
    while True:
        try:
            event = input().split()
            if event[0] == 'die':
                event[1] = int(event[1])
            else:
                event[1] = int(event[1])
                event[2] = int(event[2])
            events.append(event)
        except EOFError:
            break

    result = calculate_final_amount(events)
    print("{:.8f}".format(result))

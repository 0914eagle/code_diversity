
def calculate_final_sale(events):
    # Initialize variables
    total_cost = 0
    total_shares = 0
    average_cost = 0
    tax_rate = 0.3

    # Iterate through the events
    for event in events:
        if event[0] == "buy":
            total_cost += event[1] * event[2]
            total_shares += event[1]
            average_cost = total_cost / total_shares
        elif event[0] == "sell":
            total_shares -= event[1]
            average_cost = total_cost / total_shares
        elif event[0] == "split":
            total_shares *= event[1]
            average_cost = total_cost / total_shares
        elif event[0] == "merge":
            total_shares = (total_shares // event[1]) * event[1]
            average_cost = total_cost / total_shares
        elif event[0] == "die":
            total_profit = event[1] * total_shares - total_cost
            tax = total_profit * tax_rate
            return total_profit - tax

    return 0

def main():
    events = []
    while True:
        line = input()
        if line == "":
            break
        event = line.split()
        events.append(event)

    print(calculate_final_sale(events))

if __name__ == '__main__':
    main()


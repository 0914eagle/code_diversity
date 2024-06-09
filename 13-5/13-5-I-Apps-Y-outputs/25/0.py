
def get_tax_amount(profit, tax_rate):
    return profit * tax_rate

def get_average_cost(total_cost, number_of_shares):
    return total_cost / number_of_shares

def get_final_sale_price(average_cost, tax_rate):
    profit = average_cost * (1 - tax_rate)
    return average_cost + profit

def get_number_of_shares_after_split(number_of_shares, split_factor):
    return number_of_shares * split_factor

def get_number_of_shares_after_merge(number_of_shares, merge_factor):
    return number_of_shares // merge_factor

def get_total_cost_after_split(total_cost, split_factor):
    return total_cost * split_factor

def get_total_cost_after_merge(total_cost, merge_factor):
    return total_cost // merge_factor

def get_profit_after_sale(sale_price, average_cost):
    return sale_price - average_cost

def get_tax_amount_after_sale(profit, tax_rate):
    return profit * tax_rate

def get_final_sale_price_after_tax(sale_price, tax_amount):
    return sale_price - tax_amount

def main():
    number_of_shares = 0
    total_cost = 0
    average_cost = 0
    tax_rate = 0.3
    tax_amount = 0
    profit = 0
    sale_price = 0
    final_sale_price = 0
    for event in events:
        if event[0] == "buy":
            number_of_shares += event[1]
            total_cost += event[2] * event[1]
            average_cost = get_average_cost(total_cost, number_of_shares)
        elif event[0] == "sell":
            profit = get_profit_after_sale(event[2], average_cost)
            tax_amount = get_tax_amount_after_sale(profit, tax_rate)
            final_sale_price = get_final_sale_price_after_tax(event[2], tax_amount)
            number_of_shares -= event[1]
            total_cost -= event[2] * event[1]
            average_cost = get_average_cost(total_cost, number_of_shares)
        elif event[0] == "split":
            number_of_shares = get_number_of_shares_after_split(number_of_shares, event[1])
            total_cost = get_total_cost_after_split(total_cost, event[1])
            average_cost = get_average_cost(total_cost, number_of_shares)
        elif event[0] == "merge":
            number_of_shares = get_number_of_shares_after_merge(number_of_shares, event[1])
            total_cost = get_total_cost_after_merge(total_cost, event[1])
            average_cost = get_average_cost(total_cost, number_of_shares)
        elif event[0] == "die":
            sale_price = event[1]
            profit = get_profit_after_sale(sale_price, average_cost)
            tax_amount = get_tax_amount_after_sale(profit, tax_rate)
            final_sale_price = get_final_sale_price_after_tax(sale_price, tax_amount)
    print(final_sale_price)

if __name__ == '__main__':
    main()



import sys

def get_input():
    input_list = []
    for line in sys.stdin:
        input_list.append(line.strip())
    return input_list

def get_shares(input_list):
    shares = 0
    for event in input_list:
        if event.startswith("buy"):
            shares += int(event.split()[1])
        elif event.startswith("sell"):
            shares -= int(event.split()[1])
    return shares

def get_average_cost(input_list):
    total_cost = 0
    total_shares = 0
    for event in input_list:
        if event.startswith("buy"):
            total_cost += int(event.split()[2]) * int(event.split()[1])
            total_shares += int(event.split()[1])
    return total_cost / total_shares

def get_profit(input_list, shares, average_cost):
    profit = 0
    for event in input_list:
        if event.startswith("sell"):
            profit += int(event.split()[2]) * int(event.split()[1])
    return profit - (shares * average_cost)

def get_tax(profit):
    return profit * 0.3

def get_final_sale_price(input_list, profit, tax):
    final_sale_price = 0
    for event in input_list:
        if event.startswith("die"):
            final_sale_price = int(event.split()[1])
            break
    return final_sale_price - tax

def solve(input_list):
    shares = get_shares(input_list)
    average_cost = get_average_cost(input_list)
    profit = get_profit(input_list, shares, average_cost)
    tax = get_tax(profit)
    final_sale_price = get_final_sale_price(input_list, profit, tax)
    return final_sale_price

if __name__ == '__main__':
    input_list = get_input()
    print(solve(input_list))


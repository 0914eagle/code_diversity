
def get_max_profit(buns, patties, cutlets, hamburger_price, chicken_price):
    # Calculate the maximum number of hamburgers that can be sold
    max_hamburgers = min(buns // 2, patties)
    # Calculate the maximum number of chicken burgers that can be sold
    max_chicken_burgers = min(buns // 2, cutlets)
    # Calculate the total profit
    total_profit = (max_hamburgers * hamburger_price) + (max_chicken_burgers * chicken_price)
    return total_profit

def main():
    # Read the number of queries
    num_queries = int(input())
    # Loop through each query
    for _ in range(num_queries):
        # Read the input
        buns, patties, cutlets = map(int, input().split())
        hamburger_price, chicken_price = map(int, input().split())
        # Calculate the maximum profit
        max_profit = get_max_profit(buns, patties, cutlets, hamburger_price, chicken_price)
        # Print the result
        print(max_profit)

if __name__ == '__main__':
    main()


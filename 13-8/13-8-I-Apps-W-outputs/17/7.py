
def get_max_profit(buns, beef_patties, chicken_cutlets, hamburger_price, chicken_burger_price):
    # Calculate the maximum number of hamburgers that can be sold
    max_hamburgers = min(buns // 2, beef_patties)
    # Calculate the maximum number of chicken burgers that can be sold
    max_chicken_burgers = min(buns // 2, chicken_cutlets)
    # Calculate the total income
    total_income = (max_hamburgers * hamburger_price) + (max_chicken_burgers * chicken_burger_price)
    return total_income

def main():
    # Read the number of queries
    num_queries = int(input())
    # Iterate over each query
    for _ in range(num_queries):
        # Read the input for the query
        buns, beef_patties, chicken_cutlets, hamburger_price, chicken_burger_price = map(int, input().split())
        # Calculate the maximum profit for the query
        max_profit = get_max_profit(buns, beef_patties, chicken_cutlets, hamburger_price, chicken_burger_price)
        # Print the maximum profit
        print(max_profit)

if __name__ == '__main__':
    main()


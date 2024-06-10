
def get_max_profit(buns, patties, chicken, hamburger_price, chicken_price):
    # Calculate the maximum number of hamburgers that can be made
    max_hamburgers = int(buns / 2)
    # Calculate the maximum number of chicken burgers that can be made
    max_chicken_burgers = int(buns / 2)
    # Calculate the maximum profit that can be achieved
    max_profit = (max_hamburgers * hamburger_price) + (max_chicken_burgers * chicken_price)
    return max_profit

def main():
    # Read the number of queries
    queries = int(input())
    # Loop through each query
    for _ in range(queries):
        # Read the number of buns, patties, and chicken
        buns, patties, chicken = map(int, input().split())
        # Read the hamburger and chicken burger prices
        hamburger_price, chicken_price = map(int, input().split())
        # Calculate the maximum profit
        max_profit = get_max_profit(buns, patties, chicken, hamburger_price, chicken_price)
        # Print the maximum profit
        print(max_profit)

if __name__ == '__main__':
    main()


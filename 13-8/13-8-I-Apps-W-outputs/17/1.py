
def get_max_profit(buns, patties, cutlets, hamburger_price, chicken_price):
    # Calculate the maximum number of hamburgers that can be made
    max_hamburgers = min(buns // 2, patties)
    # Calculate the maximum number of chicken burgers that can be made
    max_chicken_burgers = min(buns // 2, cutlets)
    # Calculate the total profit
    total_profit = (max_hamburgers * hamburger_price) + (max_chicken_burgers * chicken_price)
    return total_profit

def main():
    queries = int(input())
    for _ in range(queries):
        buns, patties, cutlets = map(int, input().split())
        hamburger_price, chicken_price = map(int, input().split())
        print(get_max_profit(buns, patties, cutlets, hamburger_price, chicken_price))

if __name__ == '__main__':
    main()


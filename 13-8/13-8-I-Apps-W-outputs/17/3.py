
def get_max_profit(buns, beef_patties, chicken_cutlets, hamburger_price, chicken_burger_price):
    # Calculate the maximum number of hamburgers and chicken burgers that can be made
    max_hamburgers = min(buns // 2, beef_patties)
    max_chicken_burgers = min(buns // 2, chicken_cutlets)
    
    # Calculate the total income
    total_income = (max_hamburgers * hamburger_price) + (max_chicken_burgers * chicken_burger_price)
    
    return total_income

def main():
    queries = int(input())
    
    for i in range(queries):
        buns, beef_patties, chicken_cutlets = map(int, input().split())
        hamburger_price, chicken_burger_price = map(int, input().split())
        print(get_max_profit(buns, beef_patties, chicken_cutlets, hamburger_price, chicken_burger_price))
        
if __name__ == '__main__':
    main()


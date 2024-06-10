
def get_maximum_profit(buns, patties, cutlets, hamburger_price, chicken_price):
    hamburgers = min(buns // 2, patties)
    chicken_burgers = min(buns // 2, cutlets)
    total_income = hamburgers * hamburger_price + chicken_burgers * chicken_price
    return total_income

def main():
    queries = int(input())
    for _ in range(queries):
        buns, patties, cutlets = map(int, input().split())
        hamburger_price, chicken_price = map(int, input().split())
        print(get_maximum_profit(buns, patties, cutlets, hamburger_price, chicken_price))

if __name__ == '__main__':
    main()


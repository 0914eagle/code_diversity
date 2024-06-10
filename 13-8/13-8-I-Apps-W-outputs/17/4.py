
def get_max_profit(buns, patties, cutlets, hamburger_price, chicken_price):
    hamburgers = buns // 2
    chicken_burgers = buns // 2
    if patties < hamburgers:
        hamburgers = patties
    if cutlets < chicken_burgers:
        chicken_burgers = cutlets
    return hamburgers * hamburger_price + chicken_burgers * chicken_price

def main():
    num_queries = int(input())
    for _ in range(num_queries):
        buns, patties, cutlets = map(int, input().split())
        hamburger_price, chicken_price = map(int, input().split())
        print(get_max_profit(buns, patties, cutlets, hamburger_price, chicken_price))

if __name__ == '__main__':
    main()


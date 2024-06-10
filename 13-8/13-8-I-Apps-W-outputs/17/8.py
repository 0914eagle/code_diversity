
def get_max_profit(buns, patties, cutlets, h_price, c_price):
    h_burgers = min(buns // 2, patties)
    c_burgers = min(buns // 2, cutlets)
    return h_burgers * h_price + c_burgers * c_price

def main():
    num_queries = int(input())
    for _ in range(num_queries):
        buns, patties, cutlets = map(int, input().split())
        h_price, c_price = map(int, input().split())
        print(get_max_profit(buns, patties, cutlets, h_price, c_price))

if __name__ == '__main__':
    main()


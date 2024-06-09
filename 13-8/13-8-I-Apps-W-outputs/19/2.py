
def get_sellers_valera_can_deal_with(n, v, sellers):
    sellers_can_deal_with = []
    for seller in sellers:
        if seller["price"] <= v:
            sellers_can_deal_with.append(seller["id"])
    return sellers_can_deal_with

n, v = map(int, input().split())
sellers = []
for i in range(n):
    k, *prices = map(int, input().split())
    for j, price in enumerate(prices, start=1):
        sellers.append({"id": i, "price": price})

sellers_can_deal_with = get_sellers_valera_can_deal_with(n, v, sellers)
print(len(sellers_can_deal_with))
print(*sellers_can_deal_with)


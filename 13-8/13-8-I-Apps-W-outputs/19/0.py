
def get_sellers_with_deal(n, v, sellers):
    sellers_with_deal = []
    for i, seller in enumerate(sellers, start=1):
        if v >= seller:
            sellers_with_deal.append(i)
    return sellers_with_deal


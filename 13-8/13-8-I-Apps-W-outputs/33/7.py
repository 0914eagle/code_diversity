
def get_ticket_price(x, c_1, c_2):
    if x == 1:
        return c_1
    else:
        return c_1 + c_2 * (x - 1) ** 2

def get_min_price(n, c_1, c_2, visitors):
    adults = sum(visitors)
    groups = []
    for i in range(1, adults + 1):
        groups.append(i)
    min_price = float('inf')
    for group_size in groups:
        price = 0
        for i in range(n):
            if visitors[i] == 1:
                price += get_ticket_price(group_size, c_1, c_2)
        min_price = min(min_price, price)
    return min_price

if __name__ == '__main__':
    n, c_1, c_2 = map(int, input().split())
    visitors = list(map(int, input()))
    print(get_min_price(n, c_1, c_2, visitors))


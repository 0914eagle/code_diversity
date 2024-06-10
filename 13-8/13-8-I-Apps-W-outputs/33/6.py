
def get_group_size(n):
    if n == 1:
        return 1
    else:
        return 2

def get_ticket_price(n, c1, c2):
    if n == 1:
        return c1
    else:
        return c1 + c2 * (n - 1) ** 2

def get_min_price(n, c1, c2, visitors):
    groups = []
    for i in range(n):
        if visitors[i] == 0:
            groups.append(get_group_size(i + 1))
    return sum(get_ticket_price(group, c1, c2) for group in groups)

def main():
    n, c1, c2 = map(int, input().split())
    visitors = list(map(int, input()))
    print(get_min_price(n, c1, c2, visitors))

if __name__ == '__main__':
    main()


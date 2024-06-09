
def get_max_money(n, m, coupons):
    # Initialize a dictionary to store the number of occurrences of each number
    num_occurrences = {}
    for q, w in coupons:
        if q not in num_occurrences:
            num_occurrences[q] = 0
        num_occurrences[q] += 1

    # Initialize a list to store the maximum number of occurrences for each number
    max_occurrences = [0] * (n + 1)
    for i in range(1, n + 1):
        max_occurrences[i] = max(max_occurrences[i - 1], num_occurrences.get(i, 0))

    # Initialize a list to store the maximum amount of money that can be paid for each number
    max_money = [0] * (n + 1)
    for i in range(1, n + 1):
        max_money[i] = max_occurrences[i] * i

    # Initialize a variable to store the maximum amount of money that can be paid in total
    total_max_money = 0

    # Iterate through the coupons and update the maximum amount of money that can be paid for each number
    for q, w in coupons:
        total_max_money += w * max_occurrences[q]
        max_money[q] = 0

    # Iterate through the numbers and update the maximum amount of money that can be paid in total
    for i in range(1, n + 1):
        total_max_money += max_money[i]

    return total_max_money

if __name__ == '__main__':
    n, m = map(int, input().split())
    coupons = []
    for _ in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(get_max_money(n, m, coupons))


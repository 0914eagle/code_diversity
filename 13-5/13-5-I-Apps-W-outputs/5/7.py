
def get_total_money(n, p, buyers):
    total_money = 0
    for i in range(n):
        if buyers[i] == "half":
            total_money += p
        elif buyers[i] == "halfplus":
            total_money += p + p//2
    return total_money

def main():
    n, p = map(int, input().split())
    buyers = []
    for i in range(n):
        buyers.append(input())
    total_money = get_total_money(n, p, buyers)
    print(total_money)

if __name__ == '__main__':
    main()


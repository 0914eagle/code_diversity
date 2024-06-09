
def get_total_money(n, p, buyers):
    # Calculate the total number of apples sold
    total_apples = 0
    for buyer in buyers:
        if buyer == "half":
            total_apples += 1
        elif buyer == "halfplus":
            total_apples += 2
    
    # Calculate the total money earned
    total_money = total_apples * p
    
    return total_money

def main():
    n, p = map(int, input().split())
    buyers = []
    for _ in range(n):
        buyers.append(input())
    
    total_money = get_total_money(n, p, buyers)
    print(total_money)

if __name__ == '__main__':
    main()


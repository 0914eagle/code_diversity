
def get_min_amount(citizens, welfare):
    # Sort the welfare of citizens in non-decreasing order
    welfare.sort()
    # Initialize the minimum amount to spend
    min_amount = 0
    # Loop through each citizen and add their welfare to the minimum amount
    for i in range(len(citizens)):
        min_amount += welfare[i]
    return min_amount

def main():
    n = int(input())
    welfare = list(map(int, input().split()))
    print(get_min_amount(n, welfare))

if __name__ == '__main__':
    main()


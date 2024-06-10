
def get_citizens_welfare(citizens):
    return sum(citizens)

def get_minimum_charges(citizens, total_burles):
    citizens_welfare = get_citizens_welfare(citizens)
    if citizens_welfare == total_burles:
        return 0
    elif citizens_welfare < total_burles:
        return total_burles - citizens_welfare
    else:
        return total_burles

def main():
    n = int(input())
    citizens = list(map(int, input().split()))
    total_burles = sum(citizens)
    minimum_charges = get_minimum_charges(citizens, total_burles)
    print(minimum_charges)

if __name__ == '__main__':
    main()


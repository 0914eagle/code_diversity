
def get_total_value(values, units, exchange_rate):
    total_value = 0
    for value, unit in zip(values, units):
        if unit == "JPY":
            total_value += value
        elif unit == "BTC":
            total_value += value * exchange_rate
        else:
            raise ValueError("Invalid unit")
    return total_value

def main():
    values = [int(input()) for _ in range(int(input()))]
    units = [input() for _ in range(int(input()))]
    exchange_rate = 380000.0
    total_value = get_total_value(values, units, exchange_rate)
    print(total_value)

if __name__ == '__main__':
    main()


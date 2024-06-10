
def convert_bitcoins(x_bitcoins):
    return x_bitcoins * 380000.0

def calculate_total_value(x_values, u_values):
    total_value = 0.0
    for x, u in zip(x_values, u_values):
        if u == "JPY":
            total_value += float(x)
        elif u == "BTC":
            total_value += convert_bitcoins(float(x))
    return total_value

def main():
    n = int(input())
    x_values = []
    u_values = []
    for i in range(n):
        x, u = input().split()
        x_values.append(x)
        u_values.append(u)
    total_value = calculate_total_value(x_values, u_values)
    print(total_value)

if __name__ == '__main__':
    main()


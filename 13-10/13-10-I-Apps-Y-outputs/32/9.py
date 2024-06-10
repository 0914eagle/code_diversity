
def get_jpy_value(bitcoins, rate):
    return bitcoins * rate

def get_total_value(x_values, u_values, rate):
    total_value = 0
    for x, u in zip(x_values, u_values):
        if u == "JPY":
            total_value += x
        else:
            total_value += get_jpy_value(x, rate)
    return total_value

def main():
    N = int(input())
    x_values = []
    u_values = []
    for i in range(N):
        x, u = input().split()
        x_values.append(float(x))
        u_values.append(u)
    rate = 380000.0
    total_value = get_total_value(x_values, u_values, rate)
    print(total_value)

if __name__ == '__main__':
    main()


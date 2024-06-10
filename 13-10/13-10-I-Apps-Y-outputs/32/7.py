
def convert_to_yen(x, u):
    if u == "JPY":
        return x
    elif u == "BTC":
        return x * 380000.0
    else:
        raise ValueError("Invalid unit of measurement")

def calculate_total_value(N, x_list, u_list):
    total_value = 0
    for i in range(N):
        total_value += convert_to_yen(x_list[i], u_list[i])
    return total_value

def main():
    N = int(input())
    x_list = []
    u_list = []
    for i in range(N):
        x, u = input().split()
        x_list.append(float(x))
        u_list.append(u)
    total_value = calculate_total_value(N, x_list, u_list)
    print(total_value)

if __name__ == '__main__':
    main()


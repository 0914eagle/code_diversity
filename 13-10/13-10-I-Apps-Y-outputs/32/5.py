
def convert_bitcoins_to_yen(bitcoins, exchange_rate):
    return bitcoins * exchange_rate

def get_total_value(exchange_rate, otoshidama_list):
    total_value = 0
    for x, u in otoshidama_list:
        if u == "JPY":
            total_value += x
        elif u == "BTC":
            total_value += convert_bitcoins_to_yen(x, exchange_rate)
    return total_value

if __name__ == '__main__':
    N = int(input())
    otoshidama_list = []
    for i in range(N):
        x, u = input().split()
        otoshidama_list.append((float(x), u))
    exchange_rate = 380000.0
    total_value = get_total_value(exchange_rate, otoshidama_list)
    print(total_value)


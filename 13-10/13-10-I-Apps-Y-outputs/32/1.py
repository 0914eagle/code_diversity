
def convert_to_yen(bitcoin_amount, btc_to_yen_rate):
    return bitcoin_amount * btc_to_yen_rate

def calculate_total_amount(otoshidama_list, btc_to_yen_rate):
    total_amount = 0
    for otoshidama in otoshidama_list:
        if otoshidama[1] == "JPY":
            total_amount += int(otoshidama[0])
        elif otoshidama[1] == "BTC":
            total_amount += convert_to_yen(float(otoshidama[0]), btc_to_yen_rate)
        else:
            raise ValueError("Invalid currency type")
    return total_amount

def main():
    btc_to_yen_rate = 380000.0
    otoshidama_list = []
    N = int(input())
    for i in range(N):
        otoshidama_list.append(input().split())
    total_amount = calculate_total_amount(otoshidama_list, btc_to_yen_rate)
    print(total_amount)

if __name__ == '__main__':
    main()


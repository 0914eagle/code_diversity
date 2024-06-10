
def convert_to_yen(bitcoins, rate):
    return bitcoins * rate

def calculate_total_yen(otoshidama):
    total = 0
    for x, u in otoshidama:
        if u == "JPY":
            total += x
        elif u == "BTC":
            total += convert_to_yen(x, 380000.0)
    return total

def main():
    num_relatives = int(input())
    otoshidama = []
    for i in range(num_relatives):
        x, u = input().split()
        otoshidama.append((float(x), u))
    print(calculate_total_yen(otoshidama))

if __name__ == '__main__':
    main()


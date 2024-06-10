
def input_data():
    N = int(input())
    data = []
    for i in range(N):
        x, u = input().split()
        data.append((float(x), u))
    return data

def convert_bitcoins(data, bitcoin_rate):
    total = 0
    for x, u in data:
        if u == 'BTC':
            total += x * bitcoin_rate
        else:
            total += x
    return total

def main():
    data = input_data()
    bitcoin_rate = 380000.0
    total = convert_bitcoins(data, bitcoin_rate)
    print(total)

if __name__ == '__main__':
    main()


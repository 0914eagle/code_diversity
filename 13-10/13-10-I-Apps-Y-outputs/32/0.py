
def get_total_value(otoshidama_list):
    total_value = 0
    for otoshidama in otoshidama_list:
        if otoshidama[1] == "JPY":
            total_value += int(otoshidama[0])
        else:
            total_value += int(otoshidama[0] * 380000)
    return total_value

def main():
    n = int(input())
    otoshidama_list = []
    for i in range(n):
        otoshidama = input().split()
        otoshidama_list.append(otoshidama)
    total_value = get_total_value(otoshidama_list)
    print(total_value)

if __name__ == '__main__':
    main()


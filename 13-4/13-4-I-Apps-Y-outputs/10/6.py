
def get_available_mb(x, n, p_list):
    available_mb = x
    for i in range(n):
        available_mb += p_list[i]
        available_mb = min(available_mb, x)
    return available_mb

def main():
    x = int(input())
    n = int(input())
    p_list = []
    for i in range(n):
        p_list.append(int(input()))
    available_mb = get_available_mb(x, n, p_list)
    print(available_mb)

if __name__ == '__main__':
    main()



def is_coins_enough(k, x):
    return sum(500 * k) >= x

def main():
    k, x = map(int, input().split())
    print("Yes") if is_coins_enough(k, x) else print("No")

if __name__ == '__main__':
    main()


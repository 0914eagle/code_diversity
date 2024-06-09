
def get_coins(k, x):
    if k * 500 >= x:
        return "Yes"
    else:
        return "No"

def main():
    k, x = map(int, input().split())
    print(get_coins(k, x))

if __name__ == '__main__':
    main()


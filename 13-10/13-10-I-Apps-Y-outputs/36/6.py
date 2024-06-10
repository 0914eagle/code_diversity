
def get_base_2_rep(n):
    if n == 0:
        return "0"
    rep = ""
    while n != 0:
        if n % 2 == 0:
            rep = "0" + rep
        else:
            rep = "1" + rep
        n //= -2
    return rep

def main():
    n = int(input())
    print(get_base_2_rep(n))

if __name__ == '__main__':
    main()


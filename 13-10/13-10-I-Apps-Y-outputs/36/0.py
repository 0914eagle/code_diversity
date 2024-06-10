
def find_base_2_representation(n):
    if n == 0:
        return "0"
    s = ""
    while n != 0:
        if n % 2 == 0:
            s = "0" + s
            n //= 2
        else:
            s = "1" + s
            n = n - 1
    return s

def main():
    n = int(input())
    print(find_base_2_representation(n))

if __name__ == '__main__':
    main()


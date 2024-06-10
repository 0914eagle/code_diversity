
def get_base_2_representation(n):
    if n == 0:
        return "0"
    result = ""
    while n != 0:
        if n % 2 == 0:
            result += "0"
        else:
            result += "1"
        n //= -2
    return result[::-1]

def main():
    n = int(input())
    print(get_base_2_representation(n))

if __name__ == '__main__':
    main()


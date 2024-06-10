
def get_base_2_representation(n):
    if n == 0:
        return "0"
    result = ""
    while n != 0:
        result = str(n % 2) + result
        n //= 2
    return result

def get_base_2_representation_recursive(n):
    if n == 0:
        return "0"
    return str(n % 2) + get_base_2_representation_recursive(n // 2)

def main():
    n = int(input())
    print(get_base_2_representation(n))
    print(get_base_2_representation_recursive(n))

if __name__ == '__main__':
    main()


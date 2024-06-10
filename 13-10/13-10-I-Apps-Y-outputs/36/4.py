
def get_base_2_representation(n):
    if n == 0:
        return "0"
    res = ""
    while n != 0:
        res += str(n % 2)
        n //= 2
    return res[::-1]

def get_base_2_representation_from_input():
    n = int(input())
    return get_base_2_representation(n)

if __name__ == '__main__':
    print(get_base_2_representation_from_input())


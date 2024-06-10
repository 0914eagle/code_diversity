
def get_base_2_representation(n):
    if n == 0:
        return "0"
    repr_list = []
    while n != 0:
        if n % 2 == 0:
            repr_list.append("0")
        else:
            repr_list.append("1")
        n //= 2
    return "".join(repr_list[::-1])

def solve(n):
    return get_base_2_representation(n)

if __name__ == '__main__':
    n = int(input())
    print(solve(n))



def get_base_2_representation(n):
    if n == 0:
        return "0"
    base_2_representation = ""
    while n != 0:
        if n % 2 == 0:
            base_2_representation = "0" + base_2_representation
        else:
            base_2_representation = "1" + base_2_representation
        n = n // 2
    return base_2_representation

def get_base_2_representation_2(n):
    if n == 0:
        return "0"
    base_2_representation = ""
    while n != 0:
        if n % -2 == 0:
            base_2_representation = "1" + base_2_representation
        else:
            base_2_representation = "0" + base_2_representation
        n = n // -2
    return base_2_representation

if __name__ == '__main__':
    n = int(input())
    print(get_base_2_representation(n))
    print(get_base_2_representation_2(n))


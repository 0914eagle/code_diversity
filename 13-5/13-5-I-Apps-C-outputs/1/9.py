
def convert_to_base(n, b):
    if n == 0:
        return "0"
    digits = ""
    while n > 0:
        digits = str(n % b) + digits
        n //= b
    return digits

def find_largest_base(y, ell):
    for b in range(y, 10):
        if convert_to_base(y, b).isdigit() and int(convert_to_base(y, b)) >= ell:
            return b
    return -1

if __name__ == '__main__':
    y, ell = map(int, input().split())
    print(find_largest_base(y, ell))


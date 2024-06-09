
def convert_to_base(n, b):
    if n == 0:
        return "0"
    digits = ""
    while n > 0:
        digits = str(n % b) + digits
        n //= b
    return digits

def find_largest_base(y, l):
    for b in range(y, 10):
        if all(int(c) < 10 for c in convert_to_base(y, b)) and int(convert_to_base(y, b)) >= l:
            return b
    return -1

if __name__ == '__main__':
    y, l = map(int, input().split())
    print(find_largest_base(y, l))


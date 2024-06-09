
def f1(y, l):
    # Convert y to a string in all possible bases from 2 to 16
    bases = [str(y) for b in range(2, 17) for y in [format(y, f"b")]
    # Find the largest base such that the converted string contains only decimal digits and is at least l
    for b in range(16, 2, -1):
        if all(c in "0123456789" for c in bases[b-2]) and int(bases[b-2]) >= l:
            return b
    return 0

def f2(...):
    # Your code here

if __name__ == '__main__':
    y, l = map(int, input().split())
    print(f1(y, l))


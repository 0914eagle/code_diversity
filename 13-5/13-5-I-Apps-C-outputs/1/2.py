
def f1(y, l):
    # Convert y to a string in all possible bases from 2 to 16
    bases = [str(y) for b in range(2, 17) for y in [format(y, 'b'), format(y, 'o'), format(y, 'd'), format(y, 'x')]]
    
    # Find the largest base such that the converted number contains only decimal digits and is at least l
    for b in range(len(bases)-1, -1, -1):
        if all(c in '0123456789' for c in bases[b]) and int(bases[b]) >= l:
            return b
    
    # If no suitable base is found, return 0
    return 0

def f2(...):
    # Your code here
    pass

if __name__ == '__main__':
    y, l = map(int, input().split())
    print(f1(y, l))


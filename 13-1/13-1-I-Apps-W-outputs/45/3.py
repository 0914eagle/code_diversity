
def can_transform_string(a, b):
    if a == b:
        return True
    
    if len(a) != len(b):
        return False
    
    for i in range(len(a)):
        if a[i] != b[i]:
            x = a[i]
            y = b[i]
            p = x ^ y
            q = x | y
            if p != a[i] and q != a[i] and p != b[i] and q != b[i]:
                return False
    
    return True

def main():
    a = input()
    b = input()
    print(can_transform_string(a, b))

if __name__ == '__main__':
    main()


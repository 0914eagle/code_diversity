
def is_divisibility_hack_valid(b, d):
    if b == 1 or d == 1:
        return False
    
    for m in range(1, b):
        if pow(b, m, d) == 1:
            return True
    
    return False

def main():
    b, d = map(int, input().split())
    print("yes" if is_divisibility_hack_valid(b, d) else "no")

if __name__ == '__main__':
    main()



def is_valid_divisibility_hack(b, d):
    # Base case: b = 1
    if b == 1:
        return True
    
    # Recursive case: b > 1
    if b % d == 0:
        return False
    else:
        return is_valid_divisibility_hack(b / d, d)

def main():
    b, d = map(int, input().split())
    if is_valid_divisibility_hack(b, d):
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()


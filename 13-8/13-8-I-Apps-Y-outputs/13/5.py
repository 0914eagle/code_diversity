
def plus_one(digits):
    
    return [int(i) for i in str(int("".join(map(str, digits))) + 1)]

def main():
    digits = [1, 2, 3]
    print(plus_one(digits))

if __name__ == '__main__':
    main()


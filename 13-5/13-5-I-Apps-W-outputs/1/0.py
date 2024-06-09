
def convert_to_exp_notation(x):
    a, b = str(x).split('.')
    a = int(a)
    b = len(b)
    if b == 0:
        return str(a)
    else:
        return f"{a}.{b}E{b}"

def main():
    x = input()
    print(convert_to_exp_notation(x))

if __name__ == '__main__':
    main()


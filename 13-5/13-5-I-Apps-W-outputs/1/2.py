
def get_simple_exponential_notation(x):
    a, b = str(x).split('.')
    a = int(a)
    b = len(b)
    if b == 0:
        return str(a)
    else:
        return str(a) + 'E' + str(b)

def main():
    x = input()
    print(get_simple_exponential_notation(x))

if __name__ == '__main__':
    main()


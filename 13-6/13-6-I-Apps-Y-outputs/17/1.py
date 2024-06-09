
def largest_value(a, b):
    values = [a+b, a-b, a*b]
    return max(values)

def main():
    a, b = map(int, input().split())
    print(largest_value(a, b))

if __name__ == '__main__':
    main()


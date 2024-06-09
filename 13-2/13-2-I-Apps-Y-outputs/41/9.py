
def f1(x, a):
    if x < a:
        return 0
    else:
        return 10

def f2(...):
    # Read input from stdin
    x, a = map(int, input().split())
    # Call f1 with the input
    result = f1(x, a)
    # Print the result
    print(result)

if __name__ == '__main__':
    f2()



def f1(n):
    # f1 function to input the three digit integer
    n = int(input())
    return n

def f2(n):
    # f2 function to replace the digits 1 with 9 and 9 with 1 in the input
    n = str(n)
    n = n.replace('1', '9')
    n = n.replace('9', '1')
    n = int(n)
    return n

if __name__ == '__main__':
    n = f1(n)
    print(f2(n))


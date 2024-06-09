
def f1(n):
    # find the number of 1s in the binary representation of n
    return bin(n).count("1")

def f2(n):
    # find the least number of digits 1 in the sum of addends
    addends = []
    while n > 0:
        addends.append(n % 10)
        n //= 10
    return sum(addends)

if __name__ == '__main__':
    n = int(input())
    print(f2(n))


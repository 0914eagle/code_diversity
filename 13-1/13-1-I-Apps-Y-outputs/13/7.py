
def count_ones(s):
    return sum(int(i) for i in s)

def f1(s):
    return count_ones(s)

def f2(s):
    return count_ones(s)

if __name__ == '__main__':
    s = input()
    print(f1(s))
    print(f2(s))


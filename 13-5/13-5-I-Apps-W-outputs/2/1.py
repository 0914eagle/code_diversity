
def f1(w, h):
    # Calculate the number of possible tilings
    num_tilings = (w * h) * 4
    return num_tilings

def f2(w, h):
    # Calculate the remainder when divided by 998244353
    remainder = num_tilings % 998244353
    return remainder

if __name__ == '__main__':
    w, h = map(int, input().split())
    print(f2(w, h))


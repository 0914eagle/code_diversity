
def f1(w, h):
    # Calculate the number of possible tilings
    num_tilings = 0
    for i in range(1, w+1):
        for j in range(1, h+1):
            if i == j:
                num_tilings += 1
            elif i == w-j+1:
                num_tilings += 1
            else:
                num_tilings += 2
    
    # Calculate the remainder
    remainder = num_tilings % 998244353
    
    return remainder

def f2(w, h):
    # Calculate the number of possible tilings
    num_tilings = 0
    for i in range(1, w+1):
        for j in range(1, h+1):
            if i == j:
                num_tilings += 1
            elif i == w-j+1:
                num_tilings += 1
            else:
                num_tilings += 2
    
    # Calculate the remainder
    remainder = num_tilings % 998244353
    
    return remainder

if __name__ == '__main__':
    w, h = map(int, input().split())
    print(f1(w, h))
    print(f2(w, h))


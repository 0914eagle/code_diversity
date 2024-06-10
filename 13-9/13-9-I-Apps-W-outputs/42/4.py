
def solve(a, b):
    return (1**b + 2**b + ... + a**b) % a

def main():
    a, b = map(int, input().split())
    print(solve(a, b))

if __name__ == '__main__':
    main()



def arora_mitchell_approximation(n, p, s, v):
    # c is the parameter of the algorithm that determines the running time
    c = 15
    t = s * (1 + 1/c) / v
    return t, c

def main():
    n, p, s, v = map(float, input().split())
    t, c = arora_mitchell_approximation(n, p, s, v)
    print(t)
    print(c)

if __name__ == '__main__':
    main()


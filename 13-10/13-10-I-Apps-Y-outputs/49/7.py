
def read_input():
    return [int(x) for x in input().split()]

def find_min_inspectors(N, D):
    return (N + D - 1) // D

def main():
    N, D = read_input()
    print(find_min_inspectors(N, D))

if __name__ == '__main__':
    main()


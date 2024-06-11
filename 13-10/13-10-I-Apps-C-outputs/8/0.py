
def get_maximum_sets(k, a, b):
    if a + b < k:
        return -1
    return (a + b) // k

def main():
    k, a, b = map(int, input().split())
    print(get_maximum_sets(k, a, b))

if __name__ == '__main__':
    main()

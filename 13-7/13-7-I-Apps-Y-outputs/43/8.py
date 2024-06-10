
def get_input():
    return list(map(int, input().split()))

def find_min_product(L, R):
    min_product = float('inf')
    for i in range(L, R):
        for j in range(i+1, R+1):
            product = i*j
            if product % 2019 < min_product:
                min_product = product % 2019
    return min_product

def main():
    L, R = get_input()
    print(find_min_product(L, R))

if __name__ == '__main__':
    main()


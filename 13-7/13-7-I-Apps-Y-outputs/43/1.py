
def get_min_value(L, R):
    min_value = float('inf')
    for i in range(L, R):
        for j in range(i+1, R+1):
            value = (i * j) % 2019
            if value < min_value:
                min_value = value
    return min_value

def main():
    L, R = map(int, input().split())
    print(get_min_value(L, R))

if __name__ == '__main__':
    main()



def get_input():
    return int(input())

def smallest_sum(k):
    multiple = 1
    while True:
        if (k * multiple) % 9 == 0:
            return sum(str(k * multiple))
        multiple += 1

def main():
    k = get_input()
    print(smallest_sum(k))

if __name__ == '__main__':
    main()


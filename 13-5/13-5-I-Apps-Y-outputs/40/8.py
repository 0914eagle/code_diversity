
def get_next_larger_number(x):
    x_list = [int(i) for i in str(x)]
    x_list.sort(reverse=True)
    next_larger_number = int("".join(map(str, x_list)))
    return next_larger_number

def main():
    x = int(input())
    if x == 0:
        print(0)
    else:
        print(get_next_larger_number(x))

if __name__ == '__main__':
    main()


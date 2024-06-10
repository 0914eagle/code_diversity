
def find_common_value(x_list, y_list):
    return set(x_list).intersection(y_list)

def check_conditions(x_list, y_list, x, y):
    common_value = find_common_value(x_list, y_list)
    if common_value:
        return x < common_value[0] <= y
    return False

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    if check_conditions(x_list, y_list, x, y):
        print("No War")
    else:
        print("War")

if __name__ == '__main__':
    main()


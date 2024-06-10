
def get_input():
    N, M, X, Y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    return N, M, X, Y, x_list, y_list

def is_war_break_out(N, M, X, Y, x_list, y_list):
    for x in x_list:
        if X < x <= Y:
            break
    else:
        return "War"

    for y in y_list:
        if X < y >= Y:
            break
    else:
        return "War"

    return "No War"

def main():
    N, M, X, Y, x_list, y_list = get_input()
    print(is_war_break_out(N, M, X, Y, x_list, y_list))

if __name__ == '__main__':
    main()


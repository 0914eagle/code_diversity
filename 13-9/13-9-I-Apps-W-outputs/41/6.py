
def get_speedometer_error(d_i, s_i):
    return s_i - d_i / t

def get_constant_speed_error(d_i, s_i, c):
    return s_i - (d_i / t) + c

def find_constant_speed(d_list, s_list, t):
    c_list = []
    for i in range(len(d_list)):
        c_list.append(get_constant_speed_error(d_list[i], s_list[i], c_list[i-1]))
    return c_list[-1]

def main():
    n, t = map(int, input().split())
    d_list = []
    s_list = []
    for i in range(n):
        d_i, s_i = map(int, input().split())
        d_list.append(d_i)
        s_list.append(s_i)
    c = find_constant_speed(d_list, s_list, t)
    print(c)

if __name__ == '__main__':
    main()


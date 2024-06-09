
def get_input():
    return int(input())

def solve(n):
    n_str = str(n)
    n_list = list(n_str)
    for i in range(len(n_list)):
        if n_list[i] == '1':
            n_list[i] = '9'
        elif n_list[i] == '9':
            n_list[i] = '1'
    return int(''.join(n_list))

def main():
    n = get_input()
    print(solve(n))

if __name__ == '__main__':
    main()


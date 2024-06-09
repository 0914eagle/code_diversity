
def get_input():
    return int(input())

def convert_digits(n):
    n_str = str(n)
    n_list = list(n_str)
    n_list = [9 if x == "1" else "1" for x in n_list]
    n_str = "".join(n_list)
    return int(n_str)

def main():
    n = get_input()
    print(convert_digits(n))

if __name__ == '__main__':
    main()


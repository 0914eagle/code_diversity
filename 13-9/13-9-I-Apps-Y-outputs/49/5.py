
def get_number_of_shuffles(n, type):
    if type == "out":
        return (n // 2) + (n % 2)
    else:
        return (n + 1) // 2

def main():
    while True:
        try:
            n = int(input())
            type = input()
            print(get_number_of_shuffles(n, type))
        except EOFError:
            break

if __name__ == '__main__':
    main()


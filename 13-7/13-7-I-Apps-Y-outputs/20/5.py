
def get_label(n):
    if n <= 999:
        return "ABC" + str(n).zfill(3)
    else:
        return "ABD" + str(n - 999).zfill(3)

def main():
    n = int(input())
    print(get_label(n))

if __name__ == '__main__':
    main()


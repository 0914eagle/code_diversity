
def get_label(n):
    if n <= 999:
        return "ABC"
    else:
        return "ABD"

def main():
    n = int(input())
    print(get_label(n))

if __name__ == '__main__':
    main()


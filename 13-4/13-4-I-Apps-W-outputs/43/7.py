
def get_unique_code(n, codes):
    unique_code = ""
    for i in range(n):
        unique_code += str(i)
    for code in codes:
        if code != unique_code:
            return len(unique_code) - 1
    return 0

def get_input():
    n = int(input())
    codes = []
    for i in range(n):
        codes.append(input())
    return n, codes

def main():
    n, codes = get_input()
    print(get_unique_code(n, codes))

if __name__ == '__main__':
    main()


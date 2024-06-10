
def find_substring(substring, string):
    return string.count(substring)

def main():
    N = int(input())
    T = input()
    S = "110" * 10**10
    count = find_substring(T, S)
    print(count)

if __name__ == '__main__':
    main()


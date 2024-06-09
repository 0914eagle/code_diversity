
def rotate_string(s, n):
    return s[n:] + s[:n]

def main():
    s = input()
    n = int(input())
    print(rotate_string(s, n))

if __name__ == '__main__':
    main()


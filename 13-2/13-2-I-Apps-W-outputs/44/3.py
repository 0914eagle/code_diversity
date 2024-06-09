
def rotate_string(string, n):
    return string[n:] + string[:n]

def main():
    string = input()
    n = int(input())
    print(rotate_string(string, n))

if __name__ == '__main__':
    main()


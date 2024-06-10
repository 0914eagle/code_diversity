
def get_final_string(n, m, s):
    for i in range(m):
        l, r, c1, c2 = map(int, input().split())
        s = s[:l-1] + c2 + s[r:]
    return s

def main():
    n, m = map(int, input().split())
    s = input()
    print(get_final_string(n, m, s))

if __name__ == '__main__':
    main()


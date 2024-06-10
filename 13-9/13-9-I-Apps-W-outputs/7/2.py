
def get_final_string(s, m, n):
    for i in range(m):
        l, r, c1, c2 = map(int, input().split())
        s = s[:l-1] + c2 + s[r:]
    return s

def main():
    n, m = map(int, input().split())
    s = input()
    print(get_final_string(s, m, n))

if __name__ == '__main__':
    main()


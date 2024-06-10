
def get_final_string(n, m, s, l, r, c1, c2):
    for i in range(m):
        s = s[:l-1] + c2 + s[r:]
    return s

def main():
    n, m = map(int, input().split())
    s = input()
    for i in range(m):
        l, r, c1, c2 = map(int, input().split())
        s = get_final_string(n, m, s, l, r, c1, c2)
    print(s)

if __name__ == '__main__':
    main()


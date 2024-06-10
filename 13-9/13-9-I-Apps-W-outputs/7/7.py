
def get_string_after_operations(n, m, s, operations):
    for l, r, c1, c2 in operations:
        s = s[:l-1] + c2 * (r-l+1) + s[r:]
    return s

def main():
    n, m = map(int, input().split())
    s = input()
    operations = [tuple(input().split()) for _ in range(m)]
    print(get_string_after_operations(n, m, s, operations))

if __name__ == '__main__':
    main()



def get_final_string(n, m, s, operations):
    for operation in operations:
        l, r, c_1, c_2 = operation
        s = s[:l-1] + c_2 * (r - l + 1) + s[r:]
    return s

def main():
    n, m = map(int, input().split())
    s = input()
    operations = [input().split() for _ in range(m)]
    final_string = get_final_string(n, m, s, operations)
    print(final_string)

if __name__ == '__main__':
    main()


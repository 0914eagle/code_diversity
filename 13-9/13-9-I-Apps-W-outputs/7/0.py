
def get_input():
    n, m = map(int, input().split())
    s = input()
    operations = []
    for i in range(m):
        l, r, c1, c2 = map(int, input().split())
        operations.append((l, r, c1, c2))
    return n, m, s, operations

def perform_operations(s, operations):
    for l, r, c1, c2 in operations:
        s = s[:l-1] + c2 + s[r:]
    return s

def main():
    n, m, s, operations = get_input()
    final_string = perform_operations(s, operations)
    print(final_string)

if __name__ == '__main__':
    main()


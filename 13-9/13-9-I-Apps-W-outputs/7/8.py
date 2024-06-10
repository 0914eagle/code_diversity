
def get_final_string(string, operations):
    for operation in operations:
        l, r, c1, c2 = operation
        string = string[:l-1] + c2 + string[r:]
    return string

def main():
    n, m = map(int, input().split())
    string = input()
    operations = []
    for _ in range(m):
        l, r, c1, c2 = map(int, input().split())
        operations.append((l, r, c1, c2))
    final_string = get_final_string(string, operations)
    print(final_string)

if __name__ == '__main__':
    main()



def get_correct_choice(a, b):
    if a == 1 and b == 2:
        return 3
    if a == 1 and b == 3:
        return 2
    if a == 2 and b == 1:
        return 3
    if a == 2 and b == 3:
        return 1
    if a == 3 and b == 1:
        return 2
    if a == 3 and b == 2:
        return 1

def main():
    a, b = map(int, input().split())
    print(get_correct_choice(a, b))

if __name__ == '__main__':
    main()


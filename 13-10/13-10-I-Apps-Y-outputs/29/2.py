
def solve(alpha):
    if alpha.isupper():
        return "A"
    else:
        return "a"

def main():
    alpha = input()
    print(solve(alpha))

if __name__ == '__main__':
    main()


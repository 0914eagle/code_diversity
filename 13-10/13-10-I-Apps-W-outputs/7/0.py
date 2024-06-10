
def get_welfare(citizens):
    return sum(citizens)

def equalize_welfare(citizens):
    welfare = get_welfare(citizens)
    return welfare

def main():
    n = int(input())
    citizens = list(map(int, input().split()))
    print(equalize_welfare(citizens))

if __name__ == '__main__':
    main()



def calculate_years(x):
    balance = 100
    years = 0
    while balance < x:
        balance *= 1.01
        years += 1
    return years

def main():
    x = int(input())
    print(calculate_years(x))

if __name__ == '__main__':
    main()


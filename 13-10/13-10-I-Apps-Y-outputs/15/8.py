
def get_original_task(powers, numbers):
    original_task = 0
    for i in range(len(powers)):
        original_task += numbers[i] ** int(powers[i])
    return original_task

def main():
    N = int(input())
    powers = input().split()
    numbers = [int(input()) for _ in range(N)]
    print(get_original_task(powers, numbers))

if __name__ == '__main__':
    main()


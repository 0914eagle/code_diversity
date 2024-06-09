
def check_sheep_and_wolves(num_sheep, num_wolves):
    if num_wolves >= num_sheep:
        return "unsafe"
    else:
        return "safe"

if __name__ == '__main__':
    num_sheep, num_wolves = map(int, input().split())
    print(check_sheep_and_wolves(num_sheep, num_wolves))


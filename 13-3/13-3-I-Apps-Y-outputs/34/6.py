
def get_closer_store(x, a, b):
    if abs(x - a) < abs(x - b):
        return "A"
    else:
        return "B"

if __name__ == '__main__':
    x, a, b = map(int, input().split())
    print(get_closer_store(x, a, b))


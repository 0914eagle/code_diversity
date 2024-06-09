
def get_mean(r1, r2):
    return (r1 + r2) / 2

def get_r2(r1, mean):
    return 2 * mean - r1

if __name__ == '__main__':
    r1, mean = map(int, input().split())
    r2 = get_r2(r1, mean)
    print(r2)


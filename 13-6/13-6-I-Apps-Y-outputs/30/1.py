
def get_mean(r1, r2):
    return (r1 + r2) / 2

def restore_r2(s, r1):
    r2 = s * 2 - r1
    return r2

if __name__ == '__main__':
    r1, s = map(int, input().split())
    r2 = restore_r2(s, r1)
    print(r2)


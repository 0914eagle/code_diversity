
def get_empty_bottles_count(e, f):
    return e + f

def get_sodas_count(empty_bottles_count, c):
    return empty_bottles_count // c

if __name__ == '__main__':
    e, f, c = map(int, input().split())
    empty_bottles_count = get_empty_bottles_count(e, f)
    sodas_count = get_sodas_count(empty_bottles_count, c)
    print(sodas_count)


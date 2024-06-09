
def get_finish_time(t_i, d_i, b, queries):
    if len(queries) < b:
        queries.append((t_i, d_i))
        return t_i + d_i
    else:
        return -1

def main():
    n, b = map(int, input().split())
    queries = []
    for _ in range(n):
        t_i, d_i = map(int, input().split())
        finish_time = get_finish_time(t_i, d_i, b, queries)
        print(finish_time)

if __name__ == '__main__':
    main()



def get_f_i(f_prev, k):
    if k == 1:
        return "What are you doing while sending "
    elif k == 2:
        return "\""
    elif k == 3:
        return f_prev[0]
    elif k == 4:
        return "\"? Are you busy?"
    elif k == 5:
        return " Will you send "
    elif k == 6:
        return "\""
    elif k == 7:
        return f_prev[0]
    elif k == 8:
        return "\"?"
    else:
        return "."

def get_answer(n, k):
    if n == 0:
        return "."
    else:
        f_prev = "What are you doing at the end of the world? Are you busy? Will you save us?"
        for i in range(n-1):
            f_prev = get_f_i(f_prev, k)
        return f_prev[k-1]

def main():
    q = int(input())
    for i in range(q):
        n, k = map(int, input().split())
        print(get_answer(n, k), end="")

if __name__ == '__main__':
    main()


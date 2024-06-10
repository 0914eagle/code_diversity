
def find_character(f_string, k):
    return f_string[k - 1]

def main():
    q = int(input())
    for i in range(q):
        n, k = map(int, input().split())
        if n == 0:
            f_string = "What are you doing at the end of the world? Are you busy? Will you save us?"
        else:
            f_string = "What are you doing while sending " + find_character(f_string, k - 1) + "? Are you busy? Will you send " + find_character(f_string, k - 1) + "?"
        print(find_character(f_string, k), end="")

if __name__ == '__main__':
    main()


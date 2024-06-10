
def get_concatenation_of_string(string, num_copies):
    return string * num_copies

def count_substring(string, substring):
    return string.count(substring)

def main():
    N = int(input())
    T = input()
    S = get_concatenation_of_string("110", 10**10)
    count = count_substring(S, T)
    print(count)

if __name__ == '__main__':
    main()


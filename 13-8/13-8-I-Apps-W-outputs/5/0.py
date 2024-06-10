
def concatenate_strings(string1, string2):
    return string1 + string2

def count_substring(string, substring):
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count

def main():
    N = int(input())
    T = input()
    S = concatenate_strings("110", T)
    count = count_substring(S, T)
    print(count)

if __name__ == '__main__':
    main()


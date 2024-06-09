
def count_substring(string, substring):
    return sum(1 for i in range(len(string)) if string[i:].startswith(substring))

N = int(input())
T = input()
S = "110" * 10**10
print(count_substring(S, T))


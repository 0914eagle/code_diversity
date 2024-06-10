
def how_many_times(string: str, substring: str) -> int:
    def count_overlapping_substrings(string: str, substring: str) -> int:
        count = 0
        start = 0
        while start <= len(string) - len(substring):
            if string[start:start + len(substring)] == substring:
                count += 1
                start += 1
            else:
                start += 1
        return count

    if not string or not substring:
        return 0
    return count_overlapping_substrings(string, substring)

how_many_times(input(), input())

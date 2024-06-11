def how_many_times(string: str, substring: str) -> int:
    
    if not string or not substring:
        return 0
    if len(substring) > len(string):
        return 0
    if substring == string:
        return 1
    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count


if __name__ == "__main__":
    import
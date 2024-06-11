def monotonic(l: list):
    
    if len(l) <= 1:
        return True
    if l[0] < l[1]:
        return all(l[i] <= l[i + 1] for i in range(len(l) - 1))
    else:
        return all(l[i] >= l[i + 1] for i in range(len(l) - 1))


if __name__ == "__main__":
    import doctest

def unique_digits(x):
    
    # Your code here
    return sorted(list(set(x) - set([i for i in x if '2' in str(i) or '4' in str(i) or '6' in str(i) or '8' in str(i)])))


if __name__ == '__main__':
    print("Example:")
    print(unique_digits([15, 33, 1422, 1]))

    # These "assert
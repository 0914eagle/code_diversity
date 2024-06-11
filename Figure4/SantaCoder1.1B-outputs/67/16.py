def fruit_distribution(s,n):
    
    s = s.split()
    count = 0
    for i in s:
        if i == "apples":
            count += int(n/5)
            n -= int(n/5)
        elif i == "oranges":
            count += int(n/3)
            n -= int(n/3)
    return count

if __name__ == "__main__":
    s = input()
    n = int(input())
    print(fruit_distribution(s,n))

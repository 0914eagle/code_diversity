
def findWinner(n):
    if n % 2 == 0:
        return "Petya"
    else:
        return "Vasya"

n = int(input())
print(findWinner(n))

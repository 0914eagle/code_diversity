
n, x, y = map(int, input().split())
s = input().strip()

# Count the number of transitions from 0 to 1 in the string
transitions = sum(1 for i in range(1, n) if s[i] == '1' and s[i-1] == '0')

# If there are no transitions, the cost is 0
if transitions == 0:
    print(0)
# If there is only one transition, the cost is y
elif transitions == 1:
    print(y)
# If there are more than one transition, the cost is x + y
else:
    print(x + y)

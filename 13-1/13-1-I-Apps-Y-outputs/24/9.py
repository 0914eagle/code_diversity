
N = int(input())
dice_rolls = []

for i in range(N):
    dice_rolls.append(list(map(int, input().split())))

# Check if there are at least three consecutive doublets
for i in range(N-2):
    if dice_rolls[i][0] == dice_rolls[i][1] and dice_rolls[i+1][0] == dice_rolls[i+1][1] and dice_rolls[i+2][0] == dice_rolls[i+2][1]:
        print("Yes")
        exit()

print("No")


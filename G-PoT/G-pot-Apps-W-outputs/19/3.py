
n = int(input())

# Find the maximum number of games the winner can participate in
# The winner will play against players with the least number of games played
# We pair up players with consecutive numbers to minimize the difference in games played
# The winner will play against the player with the least number of games played
# The maximum number of games will be half of the total number of players

max_games = n // 2
print(max_games)

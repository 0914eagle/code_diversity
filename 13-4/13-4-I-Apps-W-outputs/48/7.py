
def get_player_name():
    return input()

def get_number_of_cuboids():
    return int(input())

def get_cuboid_sizes():
    return tuple(map(int, input().split()))

def get_move(cuboid_sizes):
    # Your code to get the move
    pass

def play_game(player_name, number_of_cuboids, cuboid_sizes):
    if player_name == "RUBEN":
        player_name = "ALBERT"
    else:
        player_name = "RUBEN"
    return player_name

if __name__ == '__main__':
    player_name = get_player_name()
    number_of_cuboids = get_number_of_cuboids()
    cuboid_sizes = get_cuboid_sizes()
    player_name = play_game(player_name, number_of_cuboids, cuboid_sizes)
    print(player_name)


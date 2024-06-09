
def black_vienna(investigations):
    num_investigations = len(investigations)
    num_suspects = 26
    num_solutions = 0

    for i in range(num_investigations):
        suspects = investigations[i][:2]
        player = investigations[i][2]
        reply = investigations[i][3]

        if player == 1:
            num_solutions += num_suspects - reply
        else:
            num_solutions += reply

    return num_solutions


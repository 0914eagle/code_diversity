
def slugging_percentage(at_bats):
    bases = 0
    walks = 0
    for at_bat in at_bats:
        if at_bat == -1:
            walks += 1
        else:
            bases += at_bat
    return bases / (len(at_bats) - walks)


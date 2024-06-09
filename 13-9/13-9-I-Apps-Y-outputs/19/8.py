
def slugging_percentage(at_bats):
    bases = 0
    hits = 0
    for at_bat in at_bats:
        if at_bat == -1:
            continue
        bases += at_bat
        hits += 1
    return bases / hits



def find_cia_blimps(blimp_list):
    cia_blimps = []
    for i, blimp in enumerate(blimp_list):
        if "CIA" in blimp or "FBI" in blimp:
            cia_blimps.append(i)
    if not cia_blimps:
        return "HE GOT AWAY!"
    return " ".join(str(x) for x in sorted(cia_blimps))



def find_cia_blimps(blimp_list):
    cia_blimps = []
    for i, blimp in enumerate(blimp_list):
        if "CIA" in blimp or "FBI" in blimp:
            cia_blimps.append(i)
    if not cia_blimps:
        return "HE GOT AWAY!"
    return " ".join(str(cia_blimp) for cia_blimp in sorted(cia_blimps))



def find_cia_blimps(blimp_list):
    cia_blimps = []
    for i, registration in enumerate(blimp_list):
        if "CIA" in registration or "FBI" in registration:
            cia_blimps.append(i)
    if not cia_blimps:
        return "HE GOT AWAY!"
    return " ".join(str(i) for i in sorted(cia_blimps))


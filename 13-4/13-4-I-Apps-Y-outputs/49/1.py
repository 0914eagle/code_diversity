
def find_cia_blimps(registration_codes):
    cia_blimps = []
    for i, code in enumerate(registration_codes):
        if "CIA" in code or "FBI" in code:
            cia_blimps.append(i)
    if not cia_blimps:
        return "HE GOT AWAY!"
    return " ".join(str(i) for i in sorted(cia_blimps))


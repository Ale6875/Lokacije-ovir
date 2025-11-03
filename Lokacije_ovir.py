zemljevid = [
    "......",
    "..##..",
    ".##.#.",
    "...###",
    "###.##",
]

ovire = []

for y, vrstica in enumerate(zemljevid, start=1):
    i = 0
    while i < len(vrstica):
        if vrstica[i] == "#":
            zacetek = i + 1
            while i < len(vrstica) and vrstica[i] == "#":
                i += 1
            konec = i
            ovire.append((zacetek, konec, y))
        else:
            i += 1

print(ovire)
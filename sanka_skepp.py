from rutnat import visa_rutnät

print("Välkommen till Sänka Skepp!")
def läs_ruta():
    while True:
        col = int(input("Välj kolumn (1-5): "))

        rad = int(input("Välj rad (1-5): "))

        koordinater = (rad, col)

        if 1 <= rad <= 5 and 1 <= col <= 5:
            return koordinater
        else:
            print("Både rad och kolumn måste vara mellan 1 och 5.")

def läs_båt():
    while True:
        båt = []

        for nummer in range(1, 4):
            print("Välj ruta", nummer, "för din båt.")
            vald_ruta = läs_ruta()
            båt.append(vald_ruta)

        (r1, k1), (r2, k2), (r3, k3) = båt

        samma_rad = r1 == r2 == r3
        kolumner = sorted([k1, k2, k3])
        kolumner_i_följd = kolumner == [kolumner[0], kolumner[0] + 1, kolumner[0] + 2]

        samma_kolumn = k1 == k2 == k3
        rader = sorted([r1, r2, r3])
        rader_i_följd = rader == [rader[0], rader[0] + 1, rader[0] + 2]

        vågrät = samma_rad and kolumner_i_följd
        lodrät = samma_kolumn and rader_i_följd

        if vågrät or lodrät:
            return båt
        else:
            print("Välj tre rutor i följd på samma rad eller i samma kolumn.")

def placera_båtar(spelare):
    print(spelare, "Placerar sina båtar.")
    print("Placera båt 1.")
    första_båten = läs_båt()

    while True:
        print("Placera båt 2.")
        andra_båten = läs_båt()

        gemensamma_rutor = set(första_båten) & set(andra_båten)
        if gemensamma_rutor:
            print("Båtarna delar en ruta. Försök igen.")
        else:
            print("Båda båtarna är placerade.")
            return set(första_båten) | set(andra_båten)

def skjut(spelare, motståndarens_båtar, tidigare_skott):
    print(spelare, "välj en ruta att skjuta på.")
    visa_rutnät(tidigare_skott, motståndarens_båtar)
    skott = läs_ruta()
    tidigare_skott.add(skott)

    if skott in motståndarens_båtar:
        print("Träff!")
    else:
        print("Miss!")

spelare1_båtar = placera_båtar("Spelare 1")
spelare2_båtar = placera_båtar("Spelare 2")

spelare1_skott = set()
spelare2_skott = set()

while True:
    skjut("Spelare 1", spelare2_båtar, spelare1_skott)
    if spelare2_båtar.issubset(spelare1_skott):
        print("Spelare 1 vann!")
        break

    skjut("Spelare 2", spelare1_båtar, spelare2_skott)
    if spelare1_båtar.issubset(spelare2_skott):
        print("Spelare 2 vann!")
        break
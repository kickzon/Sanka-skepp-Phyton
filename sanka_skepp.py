# Hämta funktionen som visar spelplanen från rutnat.py.
from rutnat import visa_rutnät

print("Välkommen till Sänka Skepp!")

# Läs in en ruta. Samma funktion används för båtplacering och skott.
def läs_ruta():
    # Fråga igen om någon av koordinaterna ligger utanför planen.
    while True:
        col = int(input("Välj kolumn (1-5): "))

        rad = int(input("Välj rad (1-5): "))

        # Vi sparar alltid rad först, även om spelaren anger kolumn först.
        koordinater = (rad, col)

        if 1 <= rad <= 5 and 1 <= col <= 5:
            return koordinater
        else:
            print("Både rad och kolumn måste vara mellan 1 och 5.")

# Läs in tre rutor och kontrollera att de bildar en giltig båt.
def läs_båt():
    while True:
        # En tom lista gör att varje nytt försök börjar från början.
        båt = []

        # range(1, 4) ger 1, 2 och 3. Varje vald ruta läggs sist i listan.
        for nummer in range(1, 4):
            print("Välj ruta", nummer, "för din båt.")
            vald_ruta = läs_ruta()
            båt.append(vald_ruta)

        # Plocka ut rad (r) och kolumn (k) för var och en av de tre rutorna.
        (r1, k1), (r2, k2), (r3, k3) = båt

        # Vågrätt kräver samma rad och tre kolumner i följd.
        # Sorteringen gör att rutorna kan väljas i valfri ordning.
        samma_rad = r1 == r2 == r3
        kolumner = sorted([k1, k2, k3])
        kolumner_i_följd = kolumner == [kolumner[0], kolumner[0] + 1, kolumner[0] + 2]

        # Lodrätt fungerar på samma sätt med rad och kolumn ombytta.
        samma_kolumn = k1 == k2 == k3
        rader = sorted([r1, r2, r3])
        rader_i_följd = rader == [rader[0], rader[0] + 1, rader[0] + 2]

        vågrät = samma_rad and kolumner_i_följd
        lodrät = samma_kolumn and rader_i_följd

        # En giltig riktning räcker. return lämnar tillbaka båten och avslutar funktionen.
        if vågrät or lodrät:
            return båt
        else:
            print("Välj tre rutor i följd på samma rad eller i samma kolumn.")

# Placera en spelares två båtar och lämna tillbaka alla sex båtrutor.
def placera_båtar(spelare):
    print(spelare, "Placerar sina båtar.")
    print("Placera båt 1.")
    första_båten = läs_båt()

    # Båt 1 ligger kvar om spelaren behöver välja om båt 2.
    while True:
        print("Placera båt 2.")
        andra_båten = läs_båt()

        # & tar fram de rutor som finns i båda mängderna.
        gemensamma_rutor = set(första_båten) & set(andra_båten)
        if gemensamma_rutor:
            print("Båtarna delar en ruta. Försök igen.")
        else:
            print("Båda båtarna är placerade.")
            # | samlar rutorna från de två båtarna i en enda mängd.
            return set(första_båten) | set(andra_båten)

# Genomför en spelares tur och jämför skottet med motståndarens båtrutor.
def skjut(spelare, motståndarens_båtar, tidigare_skott):
    print(spelare, "välj en ruta att skjuta på.")
    # Visa spelarens tidigare skott före nästa val.
    visa_rutnät(tidigare_skott, motståndarens_båtar)
    skott = läs_ruta()
    # Spara rutan oavsett om skottet blir en träff eller en miss.
    tidigare_skott.add(skott)

    if skott in motståndarens_båtar:
        print("Träff!")
    else:
        print("Miss!")

# När spelet startar placerar spelarna båtarna på var sin spelplan.
spelare1_båtar = placera_båtar("Spelare 1")
spelare2_båtar = placera_båtar("Spelare 2")

# Varje spelare börjar med en tom skottmängd som finns kvar mellan turerna.
spelare1_skott = set()
spelare2_skott = set()

# Spelarna skjuter växelvis. Kontrollera vinst direkt efter varje skott.
while True:
    skjut("Spelare 1", spelare2_båtar, spelare1_skott)
    # issubset kontrollerar om varje båtruta finns bland spelarens skott.
    if spelare2_båtar.issubset(spelare1_skott):
        print("Spelare 1 vann!")
        break

    skjut("Spelare 2", spelare1_båtar, spelare2_skott)
    if spelare1_båtar.issubset(spelare2_skott):
        print("Spelare 2 vann!")
        break

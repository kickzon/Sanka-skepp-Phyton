# Skriv ut ett rutnät med spelarens skott mot motståndarens båtar.
def visa_rutnät(tidigare_skott, motståndarens_båtar):
    # Kolumnnumren står ovanför rutnätet. Varje rad får en egen symbollista.
    print("  1 2 3 4 5")
    for rad in range(1, 6):
        symboler = []

        # Gå igenom rutorna från vänster till höger på den aktuella raden.
        for kolumn in range(1, 6):
            ruta = (rad, kolumn)

            # . är oskjuten, X är träff och O är miss.
            # Genom att kolla skotten först hålls oskjutna båtrutor dolda.
            if ruta not in tidigare_skott:
                symboler.append(".")
            elif ruta in motståndarens_båtar:
                symboler.append("X")
            else:
                symboler.append("O")

        # Sätt mellanslag mellan symbolerna och skriv ut hela raden.
        print(rad, " ".join(symboler))

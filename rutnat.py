def visa_rutnät(tidigare_skott, motståndarens_båtar):
    print("  1 2 3 4 5")
    for rad in range(1, 6):
        symboler = []

        for kolumn in range(1, 6):
            ruta = (rad, kolumn)

            if ruta not in tidigare_skott:
                symboler.append(".")
            elif ruta in motståndarens_båtar:
                symboler.append("X")
            else:
                symboler.append("O")

        print(rad, " ".join(symboler))
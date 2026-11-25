# Sänka skepp

Ett terminalspel i Python för två spelare vid samma dator. Målet är att träffa alla sex rutor som motståndarens båtar täcker.

## Starta spelet

Du behöver Python 3. Inga extra Pythonpaket behövs. Öppna terminalen i projektmappen och kör:

```sh
python3 sanka_skepp.py
```

## Så spelar du

1. Varje spelare placerar två båtar på sin egen spelplan med 5 × 5 rutor. Varje båt ska täcka tre rutor i följd, vågrätt eller lodrätt. Spelarens båtar får inte överlappa.
2. Spelarna turas om att skjuta. Ange **kolumn först, sedan rad**. Skriv ett heltal mellan 1 och 5 per fråga och tryck Enter efter varje tal. Samma ordning gäller vid båtplacering.
3. Spelet meddelar direkt om skottet träffade. När samma spelare får sin nästa tur syns skottet i spelarens rutnät. `X` betyder träff, `O` betyder miss och `.` betyder oskjuten ruta.
4. Den som först träffar alla motståndarens båtrutor vinner.

## Testa rutnätet

Paren i tabellen anges som **(kolumn, rad)**.

| Placering | Rutor |
| --- | --- |
| Spelare 1, båt 1 | (1, 1), (2, 1), (3, 1) |
| Spelare 1, båt 2 | (1, 2), (2, 2), (3, 2) |
| Spelare 2, båt 1 | (1, 3), (2, 3), (3, 3) |
| Spelare 2, båt 2 | (1, 4), (2, 4), (3, 4) |

Låt spelare 1 skjuta på (1, 3) för en träff och spelare 2 på (5, 5) för en miss. På deras nästa tur ska spelare 1 se ett `X` på rad 3, kolumn 1, och spelare 2 ett `O` på rad 5, kolumn 5.

## Projektfiler

- [`sanka_skepp.py`](sanka_skepp.py) hanterar inmatning, båtplacering, skott och vinst.
- [`rutnat.py`](rutnat.py) skriver ut rutnätet med spelarens tidigare skott.

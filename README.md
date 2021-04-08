Template jeg har brukt og laget: https://github.com/andersFelde/Django-template

## Oppgave 1

Anntar at hvis man er 15 får man 60 kr i lønn
Bruker putter inn antall timer i uke
Lønn per time er ut ifra alder
Lønn per måned er lønn per uke \* 4 (anntar at det er 4 uker i en måned)

## Oppgave 2

Bruker litt forskjellig gray scale på rutene, føler det funker bedre
er hovedsakelig løst i css og jquery
4 like store divs ligger uttapå bilde(div med bilde som bakgrunn), og jquery setter opacity = 0 hver gang de blir klikket på

her resizet jeg bilde til 600px x 600px for at det skulle passe bedre på siden
lagde dermed en div som var like stor, og derfor passer også boksene perfekt

## Oppgave 3

Løst hovedsakelig i javascript og css
Begge barene er "progress-bars" fra bootstrap 5
Sum-bare øker med 0.5 \* terningkast i %. Man har i gjennomsnitt 20-30 kast før den er full - anntar at det er nok
er uansett ikke noe problem å tillate flere kast, bare å skru ned fra 0.5, til feks 0.2

Antall kast baren øker med 1% for hvert kast, tillater altså 100 kast. Men sum-baren kommer nesten alltid til 100 først
når sum-baren er >= 100 så disabler den "trill" knappen og man må refreshe siden

## Oppgave 4

Løst i javscript, css og python
Gjorde om litt på den forrige siden slik at den har to modes
Mode den var i forrige gang er definert i en session variabel, slik at det blir lagret selv om man lukker siden.
default er Oppgave 3

Grafen kunne kanskje vært bedre håndtert, men den funker til sin nytte. For hver verdi øker den med 10 px.

## If you don't have flask installed run

```
pip3 install django
or
pip install django
```

## To start the server

```
python manage.py runserver
```

> Website will now be accessible on http://localhost:8000

def uitvoeren(regel):
    commando = regel[0]                 # de eerste letter van de regel
    argument = regel[1:].strip('\n')    # de rest van de regel, en verwijder de Enter

    match commando:
        case 'f':  # vooruit
            t.forward(float(argument))
        case 'b':  # achteruit
            t.backward(float(argument))
        case 'l':  # naar links draaien
            t.left(float(argument))
        case 'r':  # naar rechts draaien
            t.right(float(argument))
        case 'o':  # stip maken
            t.dot(float(argument))
        case 's':  # begin met vullen
            t.begin_fill()
        case 'e':  # stop met vullen
            t.end_fill()
        case 'p':  # penkleur instellen
            t.pencolor(argument)
        case 'i':  # vulkleur instellen
            t.fillcolor(argument)
        case 'c':  # cirkel tekenen
            (rad, deg) = argument.split(',')  # split argumenten op ','
            t.circle(float(rad), float(deg))
        case 'u':  # pen optillen
            t.up()
        case 'd':  # pen neerzetten
            t.down()
        case 'g':  # ga naar een specifieke positie
            (x, y) = argument.split(',')  # split argumenten op ','
            t.goto(float(x), float(y))
        case _:  # onherkenbaar commando
            print(f"Onbekend commando: {commando}")

import turtle

# Open het bestand en voer de commando's uit
file = open("tekening.txt", "r")
s = turtle.getscreen()
t = turtle.Turtle()

while regel := file.readline():
    uitvoeren(regel)

file.close()
turtle.mainloop()

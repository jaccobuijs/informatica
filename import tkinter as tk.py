import tkinter as tk
import turtle

root = tk.Tk()
root.geometry("700x500")
canvas = tk.Canvas(root)
canvas.place(x=0, y=0, width=700, height=800)
screen = turtle.ScrolledCanvas(canvas)
screen.place(x=0, y=0, width=700, height=800)
t = turtle.RawTurtle(screen._canvas)
t.speed(6)
t.width(1)


move_label = tk.Label(root, text="Voor/Achteruit afstand:")
move_label.place(x=10, y=300)
move_entry = tk.Entry(root)
move_entry.place(x=150, y=300, width=100)

angle_label = tk.Label(root, text="Rotatie (graden):")
angle_label.place(x=10, y=330)
angle_entry = tk.Entry(root)
angle_entry.place(x=150, y=330, width=100)

def uitvoer_actie():
    try:
        distance = int(move_entry.get())
        t.forward(distance)
    except ValueError:
        print("Voer een geldig nummer in.")
        
    try:
        angle = int(angle_entry.get())
        t.left(angle)
    except ValueError:
        print("Voer een geldig nummer in.")


execute_button = tk.Button(root, text="Voer Actie Uit", command=uitvoer_actie)
execute_button.place(x=10, y=380, width=150, height=30)


draw_button = tk.Button(root, text="cirkel", command=lambda: cirkel())
draw_button.place(x=450, y=330, width=100, height=30)

draw_button = tk.Button(root, text="links", command=lambda: links())
draw_button.place(x=10, y=450, width=100, height=30)

draw_button = tk.Button(root, text="voren", command=lambda: voren())
draw_button.place(x=10, y=420, width=100, height=30)

draw_button = tk.Button(root, text="rechts", command=lambda: rechts())
draw_button.place(x=110, y=450, width=100, height=30)

draw_button = tk.Button(root, text="pen omlaag", command=lambda: teken())
draw_button.place(x=350, y=450, width=100, height=30)

draw_button = tk.Button(root, text="pen omhoog", command=lambda: teken1())
draw_button.place(x=350, y=420, width=100, height=30)

draw_button = tk.Button(root, text="reset", command=lambda: reset())
draw_button.place(x=350, y=390, width=100, height=30)

draw_button = tk.Button(root, text="vierhoek", command=lambda: squa())
draw_button.place(x=450, y=420, width=100, height=30)

draw_button = tk.Button(root, text="hexagon", command=lambda: hexa())
draw_button.place(x=450, y=450, width=100, height=30)

draw_button = tk.Button(root, text="driehoek", command=lambda: tria())
draw_button.place(x=450, y=360, width=100, height=30)

draw_button = tk.Button(root, text="octagon", command=lambda: octa())
draw_button.place(x=450, y=390, width=100, height=30)

draw_button = tk.Button(root, background='limegreen', command=lambda: limegreen())
draw_button.place(x=450, y=290, width=50, height=20)

draw_button = tk.Button(root, background='orange', command=lambda: orange())
draw_button.place(x=500, y=290, width=50, height=20)

draw_button = tk.Button(root, background='cyan', command=lambda: cyan())
draw_button.place(x=500, y=310, width=50, height=20)

draw_button = tk.Button(root, background='black', command=lambda: black())
draw_button.place(x=450, y=310, width=50, height=20)

draw_button = tk.Button(root, background='magenta', command=lambda: magenta())
draw_button.place(x=475, y=270, width=50, height=20)

def squa():
    for i in range(4):
        t.fd(50)
        t.rt(90)

def hexa():
    for i in range(6):
        t.forward(50)
        t.left(60)

def tria():
    for i in range(3):
        t.forward(50)
        t.left(120)

def octa():
    for i in range(8):
        t.forward(50)
        t.left(45)

def reset():
    t.reset()

def links():
    t.left(10)

def rechts():
    t.right(10)

def voren():
    t.forward(5)

def teken():
    t.down()

def teken1():
    t.up()

def cirkel():
    r = 50
    t.circle(r)

def orange():
    t.pencolor("orange")

def limegreen():
    t.pencolor("limegreen")

def cyan():
    t.pencolor("cyan")

def black():
    t.pencolor("black")

def magenta():
    t.pencolor("magenta")

root.mainloop()

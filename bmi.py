import tkinter as tk
from tkinter import ttk


def bereken_bmi():
    try:
        gewicht = float(gewicht_var.get())  
        lengte = float(lengte_var.get()) / 100  
        bmi = gewicht / (lengte ** 2)  
        bmi_label.configure(text=f"Je BMI is: {bmi:.2f}")  


        if bmi < 18.5:
            status_label.configure(text="Ondergewicht", background="orange")
        elif 18.5 <= bmi < 25:
            status_label.configure(text="Gezond gewicht", background="green")
        elif 25 <= bmi < 30:
            status_label.configure(text="Overgewicht", background="orange")
        else:
            status_label.configure(text="Obesitas", background="red")
    except ValueError:
        bmi_label.configure(text="voer getallen in")


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")


gewicht_label = ttk.Label(root, text="Gewicht in kg")
gewicht_label.place(x=20, y=20)
gewicht_var = tk.StringVar()
gewicht_entry = ttk.Entry(root, textvariable=gewicht_var)
gewicht_entry.place(x=150, y=20, width=200)


lengte_label = ttk.Label(root, text="Lengte in cm")
lengte_label.place(x=20, y=60)
lengte_var = tk.StringVar()
lengte_entry = ttk.Entry(root, textvariable=lengte_var)
lengte_entry.place(x=150, y=60, width=200)


bereken_btn = ttk.Button(root, text="Bereken BMI", command=bereken_bmi)
bereken_btn.place(x=150, y=100)


bmi_label = ttk.Label(root, text="Je BMI is:")
bmi_label.place(x=20, y=150)


status_label = ttk.Label(root, text="")
status_label.place(x=20, y=200, width=330, height=30)


root.mainloop()

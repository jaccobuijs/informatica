import turtle

t = turtle.Turtle()

hoek = 20
lengte = 1

for i in range(200): 
    t.fd(lengte)      
    t.lt(hoek)       
    lengte += 0.1
    hoek += -0.1

turtle.mainloop()

print("Bienvenidos al cine")
edad=(int(input("Introduzca su edad:")))

if edad<4:
    print(edad, "No hay costo")
elif edad< 18:
    print(edad, "10$")
elif edad >18:
    print(edad, "14$")
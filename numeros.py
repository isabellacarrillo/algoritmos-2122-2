num=input("Ingrese un número:")
divider_list=[]
total=0

if num.isnumeric():
    num=int(num)
    aux=num-1
    for i in range(1, num +1):
        if num % i==0:
            divider_list.append(i)
    print(divider_list)
for x in range(0,len(divider_list)):
    total=total+ divider_list[x]
print("Suma de los elementos:", total)

if total>num:
    print("El número es abundante")
else:
    print("El número no es abundante")

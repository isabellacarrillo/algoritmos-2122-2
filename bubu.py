num=int(input("Enter a number please:"))
aux=num-1
cont=0
while aux > 1:
    if num%aux==0:
     cont+=1
    aux-=1
if cont==0:
    print("The number is prime")
else:
    print("The number is not prime")


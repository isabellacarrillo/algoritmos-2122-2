n=input("Enter a number:")
aux=int(n)
f=aux-1

while f!=1:
    
    aux=aux*f
    f-=1

print(f"Resultado:{aux}")

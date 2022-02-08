currency={"Euro":"e", "Dollar":"$","Yen":"y"}
print(currency)


ask=input("What currency do you wish to use:")
if currency["Dollar"]:
    print(currency["Dollar"])
elif currency["Euro"]:
    print(currency["Euro"])
elif currency["Yen"]:
    print["Yen"]
else:
    print("Currency not available")
    

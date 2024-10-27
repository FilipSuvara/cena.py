broj=int(input("reci koliko proizvoda si kupio"))
cena=int(input("reci koliko kosta jedan proizvod"))
ukupno=broj*cena
if broj>=10 and broj<20:
    print("ukupna cena sa 10 posto popusta je",ukupno*0.9)
elif broj>=20:
    print("ukupna cena sa 20 posto popusta je",ukupno*0.8)
else:
    print("nema popusta",ukupno)

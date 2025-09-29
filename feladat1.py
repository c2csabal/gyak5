print("Add meg a három oldal hosszát!")
a = int(input("Az a hossz: "))
b = int(input("Az b hossz: "))
c = int(input("Az c hossz: "))

print()

if a + b > c or a + c > b or b + c > a:
    print("A megadott szakaszok alkothatnak háromszöget.")
else:
    print("A megadott szakaszok nem alkothatnak háromszöget.")
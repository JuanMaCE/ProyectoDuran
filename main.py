mayor = 0
residuo = 0
#paso 1 Christian Villegas
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
if (n1 > n2):
    mayor = n1
else:
    mayor = n2
print("El mayor es: ", mayor)
#Paso 2 Vyncen Lara
residuo=mayor%2
if residuo == 0:
    print("El número ",mayor," es par porque su residuo es 0")
else:
    print("El número ",mayor," es impar porque su residuo es ",residuo,)


#Paso 3 Juan Cortés
suma = 0
while suma < mayor:
    suma = suma + 1
    print(suma)
    


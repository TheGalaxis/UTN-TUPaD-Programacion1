#ACT 1

print("Hola Mundo")

#ACT 2

nombre= input("Ingrese su nombre por favor: ")
print(f"Hola {nombre}")

#ACT 3

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

#ACT 4

pi= 3.14
Radio = int(input("Ingrese el radio:"))

perimetro= pi * 2 * (Radio)

a= pi * (Radio**2)

print (f"el perimetro es: {perimetro}")
print (f"el area es: {a}")

#ACT 5

segundos = int(input("Coloque la cantidad de segundos a calcular: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas.")

#ACT 6

numero = int(input("ingrese un el numero del que desea ver su tabla de multiplicacion: "))
print (f"tabla de multipliar del numero {numero}:")
for i in range (1,11):
    print (f"{numero} x {i} = {numero * i}")

#ACT 7

num1 = int(input("Ingrese el primer número entero distinto de 0: "))
num2 = int(input("Ingrese el segundo número entero distinto de 0: "))

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")

#ACT 8

altura= float(input("ingrese su altura en metros"))
peso= float(input("ingrese su peso en kg"))
imc= peso / (altura ** 2)
print (f"Su IMC es : {imc}")

#ACT 9

temp_celcius= int(input ("Introduzca la temperatura a calcular en Celsisus: "))
calculo= (9/5) * temp_celcius + 32
print (f"La equivalencia de temperatura dada en Celcius a Fahrenheit es: {calculo}")

#ACT 10

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = (num1 + num2+ num3) / 3
print(f"El Promedio de los tres numeros es : {promedio}")
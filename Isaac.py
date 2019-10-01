#!/usr/bin/env python
# -- coding: utf-8 --

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    #print(car)
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
    

respuesta = 17
           
if respuesta != 42:
    print("Esta respuesta no es correcta")

usuarios_baneados = ['pepe charly', 'jose', 'maria']

#py2.7 raw_input()
#p3.X input()

name = input('Ìngresa un nombre de usuario: ')
if name not in usuarios_baneados:
    print(name.title() + " no esta baneado.")    
else:
    print(name.title() + " si esta baneado.")

# validar si eres mayor de edad (18) puedes votar
age = int(input("Dame tu edad"))


"""
if - elif - else
La entrada para menores de 4 años es gratuita.
La entrada para cualquier persona entre las edades de 4 y 18 años es de $50.
La entrada para cualquier persona mayor de 18 años es de $100
""" 
if age < 4:
    precio = 0
elif age < 18:
    precio = 50
else:
    precio = 100

print("La entrada te va a costar $" + str(precio))



operacion = input("Teclee la operacion")
num1 = int(input("Teclee el primer numero"))
num2 = int(input("Teclee el segundo numero"))

if operacion == "suma":
    resultado = num1 + num2
elif operacion == "resta":
    resultado = num1 - num2
elif operacion == "division":
    resultado = num1 / num2
else:
    resultado = num1 + num2

print("El resultado de la operacion " + str(operacion) + " es " + str(resultado))
# print("El resultado de la operacion {0} es {1}").format(operacion, resultado)

participantes = {
    'nombre': 'Isaac',
    'edad': 19,
    'cursos': ['Python', 'React'],
}
participantes ['telefono'] = 9818186627
print("========")


def holaMundo():
    print("Hola mundo")

holaMundo()

# paramentros
def saludarUser(username='palma'):
    print("Hola " + username) 

saludarUser()

n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese segundo numero: "))
suma = int()

def isaacsuma(n1 = 0 , n2 = 0):
    suma = n1 + n2
    print ('El total es : ' + str(suma))

isaacsuma(n1 , n2)

num = input("Introduce un número: ")
num = int(num)
if num == 0:
    print ("Este número es par.")
elif num%2 == 0:
    print ("Este numero es par")
else:
    print ("Este numero es impar")


def factorial(x,n):
 if(n>0):
  x=factorial(x,n-1)
  x=x*n
 else:
  x=1
 return x
n=int(input("ingresa un numero  \n"))
x=1
x=factorial(x,n)
print (x)


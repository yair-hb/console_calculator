import time 

print ("Hola! Bienvenido a la calculadora escrita en python y desarrollada por Yair")
time.sleep(1)
print ("Puedes encontrar mis codigos en:")
print ("https://github.com/yair-hb ")
time.sleep(0.8)

numero1= int(input ("Dime el primer numero: "))
numero2= int(input (f"Bien! Ahora dime el segundo numero: "))
print (f"De acuerdo, has escogido el {numero1} y el {numero2}")
time.sleep(1)

simbolo = input ()

simbolo = input(f"¿Qué quieres hacer con estos números? (Escribe la primera letra)\n -Sumar\n -Restar\n -Multiplicar\n -Dividir\n")

if simbolo == 's' or simbolo == 'S':
    print (f'{numero1}+{numero2}=',(numero1+numero2))
elif simbolo == 'r' or simbolo =='R':
    print (f'{numero1}-{numero2}=',(numero1-numero2))
elif simbolo == 'm' or simbolo == 'M':
    print (f'{numero1}*{numero2}=',(numero1*numero2))
elif simbolo == 'd' or simbolo == 'D':
    print (f'{numero1}/{numero2}=',(numero1/numero2))
else:
    print ('No has escrito ninguna letra correcta')
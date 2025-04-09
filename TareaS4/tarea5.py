#Algoritmo que calcule el porcentaje de un número dado. Ejemplo: ¿qué es el 15%
#de 200?
numerodado=int(input("Dime la cantidad que tienes -> "))
porcentaje=int(input(f"Dime el porcentaje que quieres que saque de {numerodado} -> "))
porcentajefinal=porcentaje*0.01
total=porcentajefinal*numerodado
print (" ")
print (f"El {porcentaje}% de {numerodado} es \n______________________\n{total}")
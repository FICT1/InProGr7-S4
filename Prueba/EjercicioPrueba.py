#Crea un algoritmo en python que permita
#leer el saladrio de un trabajador que gana por hora
#calcular su salario en base a las horas trabajadas

salario=float(input("Dime la cantidad de dinero que ganas (en dolares): "))
tiempo=int(input("Dime la cantidad de tiempo que trabajas: "))
salariofinal=salario*tiempo
print(f"Tu salario por cada horas trabajadas son: {salariofinal}$")
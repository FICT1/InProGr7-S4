Algoritmo PruebaDeProgramacion1
//Un estudiante desea conocer el monto total que deber� pagar para poder matricularse en una universidad. La instituci�n realiza tres tipos de cobros:
//Pago por prematr�cula
//Pago por matr�cula
//El 25% del valor total del semestre
	definir matricula, prematricula, semestre, total como Real
	escribir "Ingrese el valor de tu prematricula"
	leer prematricula
	escribir "Ingrese el valor de tu matricula"
	leer matricula
	escribir "Ingrese el valor de su semestre"
	leer semestre
	porcentaje_semestre=semestre*0.25
	total=prematricula+matricula+porcentaje_semestre
	escribir "*******************************************************************************"
	escribir " "
	escribir "El monto total para inscribirse en la universidad es de: " total " cordobas"
	escribir " "
	escribir "*******************************************************************************"
	
FinAlgoritmo

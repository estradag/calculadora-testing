Feature: Multiplicación de dos numeros
	Como usuario de la calculadora
	deseo realizar la multiplicación de dos numeros
	para obtener el resultado preciso

	Scenario: Multiplicación de 2 por 2
        Dado que ingreso un par de numeros
		cuando realizo la multiplicación de "2" por "2"
		entonces obtengo el resultado "4"

	Scenario: Multiplicación de 7 por 5
        Dado que ingreso un par de numeros
		cuando realizo la multiplicación de "7" por "5"
		entonces obtengo el resultado "35"

	Scenario: Multiplicación de 0 por -7
    Dado que ingreso un par de numeros
		cuando realizo la multiplicación de "0" por "-7"
		entonces obtengo el resultado "0"

    Scenario: Multiplicación de 1000 por 100
        Dado que ingreso un par de numeros
		cuando realizo la multiplicación de "1000" por "100"
		entonces obtengo el resultado "100000"

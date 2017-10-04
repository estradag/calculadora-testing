Feature: Suma de dos numeros
	Como usuario de la calculadora
	deseo realizar la suma de dos numeros
	para obtener el resultado preciso

	Scenario: Suma de 2 mas 2
        Dado que ingreso un par de numeros
		cuando realizo la suma de "2" mas "2"
		entonces obtengo el resultado "4"

	Scenario: Suma de 7 mas 5
        Dado que ingreso un par de numeros
		cuando realizo la suma de "7" mas "5"
		entonces obtengo el resultado "12"

	Scenario: Suma de 0 mas -7
        Dado que ingreso un par de numeros
		cuando realizo la suma de "0" mas "-7"
		entonces obtengo el resultado "-7"

    Scenario: Suma de 1000 mas 100
        Dado que ingreso un par de numeros
		cuando realizo la suma de "1000" mas "100"
		entonces obtengo el resultado "1100"

Feature: División de dos numeros
	Como usuario de la calculadora
	deseo realizar la multiplicación de dos numeros
	para obtener el resultado preciso

	Scenario: División de 2 entre 2
        Dado que ingreso un par de numeros
		cuando realizo la división de "2" entre "2"
		entonces obtengo el resultado "1"

	Scenario: División de 35 entre 5
        Dado que ingreso un par de numeros
		cuando realizo la división de "35" entre "5"
		entonces obtengo el resultado "7"

	Scenario: División de 70 entre -7
    Dado que ingreso un par de numeros
		cuando realizo la división de "70" entre "-7"
		entonces obtengo el resultado "-10"

    Scenario: División de 1000 entre 100
        Dado que ingreso un par de numeros
		cuando realizo la división de "1000" entre "100"
		entonces obtengo el resultado "10"

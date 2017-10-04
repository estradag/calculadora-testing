Feature: Resta de dos numeros
	Como usuario de la calculadora
	deseo realizar la resta de dos numeros
	para obtener el resultado preciso

	Scenario: Resta de 2 menos 2
		Dado que ingreso un par de numeros
		cuando realizo la resta de "2" menos "2"
		entonces obtengo el resultado "0"

    Scenario: Resta de 1 menos -5
    Dado que ingreso un par de numeros
		cuando realizo la resta de "1" menos "-5"
		entonces obtengo el resultado "6"

    Scenario: Resta de 22 menos 18
    Dado que ingreso un par de numeros
		cuando realizo la resta de "22" menos "18"
		entonces obtengo el resultado "4"

    Scenario: Resta de 67 menos 34
    Dado que ingreso un par de numeros
        cuando realizo la resta de "67" menos "34"
        entonces obtengo el resultado "33"

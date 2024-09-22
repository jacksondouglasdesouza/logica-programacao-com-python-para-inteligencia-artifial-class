def conversor_temperatura():
    while True:

        print("""
            ****** CONVERSOR DE TEMPERATURAS ******

            [ 1 ] Converter Fahrenheit para Celsius
            [ 2 ] Converter Celsius para Fahrenheit
            [ 3 ] Sair do Programa
        """)

        temperatura = int(input("""
            Qual a Conversão deseja Realiza? >>> 
        """))

        if temperatura == 1:
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

            celsius = (fahrenheit - 32) / 1.8
            print(f'A temperatura {fahrenheit:.2f} Fahrenheit convertida para Graus Celsius é de: {celsius:.2f}ºC')
        # --

        elif temperatura == 2:
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = (celsius * 1.8) + 32
            print(f"A temperatura º{celsius:.2f} em Graus Celsius, convertida para Fahrenheit é de: {fahrenheit:.2f}ºF")
        # --

        elif temperatura == 3:
            print("\n********** PRONTO! ***********")
            print("Programa Finalizado com Sucesso!")
            print("********************************")
            break
        # --

        else:
            print("Entrada inválida! Tente novamente.\n")
        # --
    # --


# --

conversor_temperatura()
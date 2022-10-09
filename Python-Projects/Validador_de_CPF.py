def validador():

    cpf = input("Digite seu CPF [Somente os números]: ")

    num1 = int(cpf[0])
    num2 = int(cpf[1])
    num3 = int(cpf[2])
    num4 = int(cpf[3])
    num5 = int(cpf[4])
    num6 = int(cpf[5])
    num7 = int(cpf[6])
    num8 = int(cpf[7])
    num9 = int(cpf[8])
    num10 = int(cpf[9])
    num11 = int(cpf[10])

    primeiro_digito = num1 * 10 + num2 * 9 + num3 * 8 + num4 * 7 + num5 * 6 + num6 * 5 + num7 * 4 + num8 * 3 + num9 * 2

    validar_1 = primeiro_digito * 10 % 11

    segundo_digito =  num1 * 11 + num2 * 10 + num3 * 9 + num4 * 8 + num5 * 7 + num6 * 6 + num7 * 5 + num8 * 4 + num9 * 3 + num10 * 2

    validar_2 = segundo_digito * 10 % 11

    if validar_1 == num10 and validar_2 == num11:
        
        print(f"\033[1;32mO CPF informado {cpf} é válido.\033[m")
    
        return True

    else:
    
        print(f"\033[1;31mO CPF informado {cpf} é invalido.\033[m")

        return False

validador()


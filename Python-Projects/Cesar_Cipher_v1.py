r = ''
while True:
    acao = int(input("\33[1;32m\nVocê deseja:\n0 - Sair \n1 - Encriptar: \n2 - Decriptar: \33[m"))
    if acao == 0:
        break
    n = int(input('\33[1;31mQual chave quer usar?\33[m '))
    if acao == 1:
        frase = input('\33[1;31mDigite a frase para ser encripitada: \33[m').strip()
        for x in range (0, len(frase)):
            r = r + chr(ord(frase[x]) + n)
            print(r, end='')
            r = ''
    if acao == 2:
        texto = input("\33[1;31mDigite a frase para ser decriptada:\33[m ").strip()

        for x in range (0, len(texto)):
            r = r + chr(ord(texto[x]) - n)
            print(r, end='')
            r = ''

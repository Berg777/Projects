print("\033[1;33mDigite 0 se deseja finalizar\033[m")
lista = []
while True:
    lista1 = str.lower(input('\033[1mDigite uma palavra para ser adicionada na lista: '))
    if lista1 == "0":
        break
    lista.append(lista1)
while True:
    opcao = int(input('[0] Sair\n[1] Crescrente \n[2] Decrescente: '))
    if opcao == 1:
        def bubble_sort(lista):
            for i in range(len(lista)):
                pronto = True
                for l in range(len(lista) - i - 1):
                    if lista[l] > lista[l + 1]:
                        lista[l], lista[l + 1] = lista[l + 1], lista[l]
                        pronto = False
                if pronto:
                    break
            return lista
        print(bubble_sort(lista))
    if opcao == 2:
        def bubble_sort(lista):
            for i in range(len(lista)):
                pronto = True
                for l in range(len(lista) - i - 1):
                    if lista[l] < lista[l + 1]:
                        lista[l], lista[l + 1] = lista[l + 1], lista[l]
                        pronto = False
                if pronto:
                    break
            return lista
        print(bubble_sort(lista))
    if opcao == 0:
        break
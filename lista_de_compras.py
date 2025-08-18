import os
compras = []

while True:
    x = input("[i]nserir item, [a]pagar item, [l]istar todos os itens ou apagar [t]udo ").lower()
    if x == "i":
        inserir_item = str(input("Insira um item na lista: "))
        compras.append(inserir_item)
        os.system("cls")
    elif x == "a":
        if len(compras) == 0:
            print("Sua lista está vazia!")
        else:
            os.system("cls")
            for indice, itemdalista in enumerate(compras, start = 1):
                print(indice, itemdalista)
            try:
                apagar_item_user = int(input("Digite o índice do item que você deseja apagar: "))
                apagar_item_real = apagar_item_user - 1
                compras.pop(apagar_item_real)
            except (ValueError, IndexError):
                print("Índice inválido")
    elif x == "l":
        if len(compras) == 0:
            print("Sua lista está vazia!")
        else:
            os.system("cls")
            for indice, itemdalista in enumerate(compras, start = 1):
                print(indice, itemdalista)
    elif x == "t":
        if len(compras) == 0:
            print("Sua lista já está vazia!")
        else:
            compras.clear()
            print("Sua lista foi apagada completamente.")
    else:
        print("Digite i, a, l ou t.")
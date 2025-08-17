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
            print("Sua lista esta vazia!")
        else:
            os.system("cls")
            for indice, itemdalista in enumerate(compras, start = 1):
                print(indice, itemdalista)
            try:
                apagar_item_user = int(input("Digite o indice do item que vc deseja apagar: "))
                apagar_item_real = apagar_item_user - 1
                compras.pop(apagar_item_real)
            except (ValueError, IndexError):
                print("Indice invalido")
    elif x == "l":
        if len(compras) == 0:
            print("Sua lista esta vazia!")
        else:
            os.system("cls")
            for indice, itemdalista in enumerate(compras, start = 1):
                print(indice, itemdalista)
    elif x == "t":
        if len(compras) == 0:
            print("Sua lista ja esta vazia!")
        else:
            compras.clear()
            print("Sua lista apagada completamente.")
    else:
        print("Digite i, a ou l.")


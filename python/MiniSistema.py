#MENU
print("INICIO")
print("Escolha qual opção deseja")
print("1: Cadastro de produtos.   2: Venda.  3: Listar todos produtos.   4: Relatorio    5:SAIR")
lista = []
estoque = []
vendas = []
contador = 0
#ESCOLHA
while True:
    try:
     entrada = int(input("Digite...: "))
    except ValueError:
        print("Digite apenas uma das opções (1, 2, 3, 4 ou 5)")
        continue
     
# 1 - CADASTRO
    if entrada == 5:
        print(f"ESTOQUE FINAL {estoque}")
        print("saindo...")
        break

    elif entrada == 1:
        produtos = {}
        line = input("Cadastre um produto").split()
        if len(line) == 2:
            nome = line[0]
            
            try:
                valor = float(line[1])
            except ValueError:
                print("apenas numeros")
                continue

            produtos['Nome'] = nome
            produtos['Valor'] = valor
            estoque.append(produtos)

        else:
            print("ERRO")
        continue
# 2 - VENDA
    elif entrada == 2:
        
        print("VENDA")
        line = input().split()
        
        if len(line) == 2:
            produto = line[0]
            try:
                valor = float(line[1])
                contador += valor
            except ValueError:
                print("apenas numeros")
                

            produto_venda = {'Nome':produto, 'Valor':valor}
            lista.append(produto_venda) 
            vendas.append(lista)
#CANCELA PRODUTO 
        
            if line[0].lower() =='cancelar':
                produto_cancela = line[1]
                encontrado = False
                for item in lista:
                    if item['Nome'] == produto_cancela:
                        lista.remove(item)
                        print(" PRODUTO CANCELADO")
                        encontrado = True

                if not encontrado:
                    print("PRODUTO NÂO ENCONTRADO")


# BUSCA ESTOQUE
        encontrado = False
        for item in estoque:
            if item['Nome'] == produto and item['Valor'] == valor:
                estoque.remove(item)
                print("Encontrado no estoque")
                encontrado = True
                break
        
            if not encontrado:
                print("produto não cadastrado no estoque!")

        continue
# 3 - LISTAR ESTOQUE
    elif entrada == 3:
        print(len(estoque) )
        print(estoque)
        continue

# 4 - LISTAR VENDAS
    elif entrada == 4:
        print("LISTA DE VENDAS")
        print(len(vendas))
        print(vendas)       
        print(f"valor de vendas {contador}")
        continue
            
            

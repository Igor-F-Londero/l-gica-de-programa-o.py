
def GerarSenha():
    import random
    import os
    print("===Gerador de senha===")    

    start = int(input("Digite 1 para iniciar o Gerador de senhas "))
     
    if start != 1:
        print("saindo '-'")
          
        
    else:    
        while start == 1:

            while True:
                senhaletras = input("Quais letras deseja usar? ")
                senhanumeros = input("Quais numeros deseja usar? ")
                simbolos = input("Quais simbolos? ")

                if len(senhaletras) <= 0:
                    print("O campo não pode ser nulo!")
                    continue
                elif len(senhanumeros) <= 0:
                    print("O campo não pode ser nulo!")
                    continue
                elif len(simbolos) <= 0:
                    print("O campo não pode ser nulo!")
                    continue
                

                senha = list(senhaletras) + list(senhanumeros) + list(simbolos)
                random.shuffle(senha)
                senhaEmb = ''.join(senha)

                local = input("De onde é a senha? ")

                print(f"A senha- {local} É :{senhaEmb}")

                #Definindo a pasta onde vou salvar
                pasta = r"c:\Users\igorf\Desktop\Faculdade\Projetinhos\nsei ainda\python\senhas"
                os.makedirs(pasta, exist_ok = True)#cria a pasta caso não for criada

                caminho = os.path.join(pasta,"senhas.txt")

            #Salva a senha no arquivo
                with open(caminho,'a') as arquivo:
                    arquivo.write(f"{local} : {senhaEmb}\n")     
                print("A senha foi salva no seguinte caminho: ",caminho)
                
                break
  
GerarSenha()









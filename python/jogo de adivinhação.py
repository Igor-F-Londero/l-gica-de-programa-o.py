import random

print("Adivinhe o numero!! Você tera 5 tentativas os numeros serão de 1 a 10")
print("Digite 0 para sair")


while True:
 tentativas = 0
 num = random.randint(1,10)
 numSecreto = num
    
 while tentativas < 5:    
    tentativa = int(input("Adivinhe o numero que estou pensando! "))
    tentativas += 1
    
    if tentativa == 0:
        print("Saindo...")
        break

    elif tentativa == numSecreto:
        print("Acertou!!! Parabéns")
        break

    elif tentativa < numSecreto:
        print("o número q estou pensando é maior")
    
    elif tentativa > numSecreto:
        print("o numero que estou pensando é menor")
 
    if tentativas < 5:
        print(f"você usou {tentativas} tentativas!!")

    else:
       print("Você usou todas as tentativas!")
    
    reptOUfin = input("gostaria de jogar novamente? digite 'sim' ou 'não'")
    
    if reptOUfin =='sim':
       continue
    
    else:
       print("Valeu por jogar ^^")
    break




        
    

    
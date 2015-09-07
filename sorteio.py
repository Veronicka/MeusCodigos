import random

print('***Sorteio de números para a Mega-Sena***\n')

again = 0

while again == 0 :
    k = 0
    num = []
    while k < 6:
        i = random.randint(1,60)
        if i in num:
            while i in num:
                i = random.randint(1,60)
            num.append(i)
        else:
            num.append(i)
        k=k+1

    num.sort()
    print("\nNúmeros sorteados da Mega-Sena\n")
    n = str(num)
    n = n.replace('[', '')
    n = n.replace(']', '')
    print(n)
    
    again =  int(input("\nDigite 0 para jogar novamente: "))
    print('---------------------------------------------')

print('\nObrigado e Boa Sorte!!!')

############################
# Eduardo Alves Martin N°8
# 1°E 18/08/2025
############################
VERMELHO = "\033[31m"
VERDE = "\033[32m"
############################

TAM_CNPJ = 18
cnpj = input("Por favor, insira o CNPJ:")
flag = True

if len(cnpj) != TAM_CNPJ:
    flag = False
elif (cnpj[2] != "." or cnpj[6] != "." or cnpj[10] != "/" or cnpj[15] != "-"):
    flag = False
else:
    for i in range(TAM_CNPJ):
        if (i != 2 and i != 6 and i != 10 and i != 15):
            c = cnpj[i]
            if not c.isdigit():
                flag = False
                break

if flag:
    print(f"{VERDE}Formato de CNPJ Válido.")
else:
    print(f"{VERMELHO}O CNPJ informado não tem um formato válido.")
############################
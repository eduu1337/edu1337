############################
# Eduardo Alves Martin N°8
# 1°E 18/08/2025
############################
TAM_CPF = 14
cpf = input("Por favor insira o CPF:")
flag = True

if(len(cpf) != 14):
    flag = False
elif((cpf[3] != ".") or (cpf[7] != ".") or (cpf[-3] != "-" )):
    flag = False

    for i in range(TAM_CPF):
        if((i != 3) or (i != 7) or (i != 11)):
            c = cpf[i]
            if(c.isdigit()):
                flag = False

if(flag):
    print("Formato de CPF Válido.")
else:
    print("O CPF informado não tem um formato válido.")
############################
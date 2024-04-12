NUMEROS = "0123456789"
LETRAS = "ABCDEF"

with open("entrada.txt", "r") as arquivo:
    for linha in arquivo:
        print(f"linha = {linha}")
        estado_atual = 0
        lexema = ""
        for caractere in linha.strip() + "\n":
            #linha 10 até 15 serviu para analisar os estados caracter por caracter.
            #foi comentado para a exibição dos tokens não ficarem confusos.
            '''
            print(f"caractere = {caractere}")
            print(f"numero = {caractere in NUMEROS}")
            print(f"letras = {caractere in LETRAS}")
            print(f"estado atual = {estado_atual}")
            '''

            #transição para número inteiro
            if caractere in NUMEROS and estado_atual == 0:
                lexema += caractere
                estado_atual = 6
            #transição para hexadecimal saindo do estado 0
            elif caractere in LETRAS and estado_atual == 0:
                lexema += caractere
                estado_atual = 25
            elif caractere == "x" and estado_atual == 25:
                lexema += caractere
                estado_atual = 23
            elif (caractere in LETRAS or caractere in NUMEROS) and estado_atual == 23:
                lexema += caractere
                estado_atual = 24 
            elif (caractere in LETRAS or caractere in NUMEROS) and estado_atual == 24:
                lexema += caractere
                estado_atual = 24 
            #continuação da transição int
            elif caractere in NUMEROS and estado_atual == 6:
                lexema += caractere
                estado_atual = 8
            #transição 2 hexadecimal saindo do estado 6
            elif caractere == "x" and estado_atual == 6:
                lexema += caractere 
                estado_atual = 23
            elif (caractere in LETRAS or caractere in NUMEROS) and estado_atual == 23:
                lexema += caractere
                estado_atual = 24
            elif (caractere in LETRAS or caractere in NUMEROS) and estado_atual == 24:
                lexema += caractere
                estado_atual = 24
            elif caractere in NUMEROS and estado_atual == 8:
                lexema += caractere
                estado_atual = 22
            elif caractere in NUMEROS and estado_atual == 22:
                lexema += caractere
                estado_atual = 45
            elif caractere in NUMEROS and estado_atual == 45:
                lexema += caractere
                estado_atual = 45
            #se dos estado 6 e 22, o caractere seguinte ser um '.', o programa para e exibe mensagem de erro
            #exemplo de número inválido: "1.0"
            elif estado_atual in [0,6] and caractere in ["x"]:
                print("invalido")
                break
            elif estado_atual in [6,22] and caractere in [".", "x"]:
                print("Número Invalido")
                break
            elif estado_atual in [8] and caractere in [".", "/", "_"]:
                print("Número Invalido")
                break
            elif estado_atual in [23] and caractere not in NUMEROS + LETRAS:
                print("ERRO: Endereço Inválido")
                break
            elif estado_atual in [6, 8, 22] and caractere not in NUMEROS:
                estado_atual = 54
                print("TK_INT")
                break
            elif estado_atual in [45] and caractere not in NUMEROS:
                estado_atual = 64
                print("TK_INT")
            elif estado_atual in [24] and caractere not in NUMEROS + LETRAS: 
                estado_atual = 55
                print("TK_END")


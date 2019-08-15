import time
import os
clear = lambda: os.system("cls")
check = False
conteudo = ""
achou: int = 0
adiMais = "S"
proMais = "S"
    #Criando um while para que o usuário possa utilizar ate quando quiser
while check == False:
    #Dando uma escolha entre 3 tarefas

    Escolha = int(input("Você quer \n 1- adicionar \n 2- procurar \n 3- apagar um registro \n"))

    #If para achar qual tarefa o usuário quer
    if Escolha == 1:
        clear()
        print("Abrindo sistema para ADICIONAR um registro...")
        time.sleep(2)

        while adiMais == "S":
            clear()
            arquivo = open('Registros.txt', 'r')
            conteudo = arquivo.readlines()
            OS = input("Insira o Sistema Operacional \n (OS)\n").upper()
            CIT = input("Insira o CIT \n (CIT-2019-XXXX) \n").upper()
            Dec = input("Quantas Detecções? \n (Quantidade) 0 caso não tenha detecções \n ").upper()
            Vul = input("Possui vulnerabilidade? \n (S/N) \n").upper()
            Rep = input("Foi reportada? \n (S/N) \n").upper()
            if Rep == "S":
                xx = input("Foi Reportada via Service Request? \n (S/N) \n").upper()
                if xx == "S":
                    Ticket = input("Informe o ticket aberto para report: \n (IMXXXXXXXX) \n")
                    Time = input("Qual foi o time responsável pelo patch? \n (Nome do Time) \n").upper()
                else:
                    if Vul == "N":
                        Ticket = str("CVE não encontrada no Qualys")
                        Time = "- "
                    elif Dec == 0:
                        Ticket = str("Report Vazio")
                        Time = "- "
                    else:
                        Ticket = str("Não Aplicável")
                        Time = "- "

            conteudo.append(OS)
            conteudo.append(" - ")
            conteudo.append(CIT)
            conteudo.append(" - ")
            conteudo.append(Dec)
            conteudo.append(" Detections")
            conteudo.append(" - ")
            conteudo.append(Vul)
            conteudo.append(" - ")
            conteudo.append(Rep)
            conteudo.append(" - ")
            conteudo.append(Ticket)
            conteudo.append(" - ")
            conteudo.append(Time)
            conteudo.append("\n")
            tempo = 5
            arquivo = open('Registros.txt', 'w')
            arquivo.writelines(conteudo)
            clear()
            while tempo != 0:
                print("Adicionando registro |")
                clear()
                print("Adicionando registro /")
                clear()
                print("Adicionando registro -")
                clear()
                print("Adicionando registro \ ")
                clear()
                tempo -= 1
            print("Tarefa concluida.\n")
            arquivo.close()
            adiMais = input("Você precisa adicionar mais algum regitro? \n (S/N) \n").upper()
    elif Escolha == 2:
        clear()
        print("Abrindo sistema para PROCURAR um registro...")
        time.sleep(2)
        while proMais == "S":
            clear()
            procurando = input("Insira o OS ou CIT para procurar o registro: \n (Uma pesquisa por vez) \n").upper()
            with open("Registros.txt", "r") as arq:
                for linha in arq:
                    if linha.find(procurando) > -1:
                        print(linha)
                        achou += 1
            print("Tarefa concluida.\n")
            if achou <= 0:
                print("Não foi encontrado nenhum registro com esse nome ou código.\n")
            elif achou == 1:
                print("Foi encontrado", achou, " registro.\n")
            else:
                print("Foram encontrados", achou, " registros.\n")
            achou = 0
            proMais = input("Você precisa procurar mais algum registro? \n (S/N) \n").upper()

    elif Escolha == 3:
        clear()
        print("Tarefa ainda não adicionada.")
        time.sleep(0)

    else:
        clear()
        Escolha = int(input("Opção Inválida, Escolha corretamente:\n1- Adicionar \n 2- Procurar \n 3- Apagar"))
    algo = input("Precisa fazer mais alguma coisa? \n (S/N) \n").upper()

    if algo == "S":
        check = False
        clear()
    else:
        clear()
        check = True
        print("DESENVOLVIDO POR ERIC KENJI - Uso livre")
        print("Até a próxima.")


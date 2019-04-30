# encoding: utf-8

#####	NAME:				ALGORITMO DE ESCALONAMENTO SHORTEST JOB FIRST (SJF)
#####	VERSION:			1.6
#####	DESCRIPTION:			O ALGORITMO APRESENTA A ORDEM DA EXECUCAO DOS PROCESSOS, CONFORME ESTRATEGIA DE ESCALONAMENTO
#####	DATE OF CREATION:		20/04/2019
#####	WRITTEN BY:			KARAN LUCIANO SILVA | JACKSON DURAES
#####	E-MAIL:				karanluciano1@gmail.com			
#####	DISTRO:				MANJARO LINUX
#####	LICENSE:			GPLv3 			
#####	PROJECT:			https://github.com/lkaranl/Vector_Clock

#█████████████████████████████████████
#████ ▄▄▄▄▄ █ ▀▀▄ ▀ ██ ██▀█ ▄▄▄▄▄ ████
#████ █   █ ███ ▄▄ ▀ █  ▄▄█ █   █ ████
#████ █▄▄▄█ █ ▄▄ █ ▄█▀▄▄█▀█ █▄▄▄█ ████
#████▄▄▄▄▄▄▄█ █ ▀ █ ▀▄█ ▀▄█▄▄▄▄▄▄▄████
#████   █▀▄▄▀▄  ██▀█▄ ▀█▀    ▄██  ████
#██████▀█▄▀▄▄ ▀█▄██  ▀██▄ ▀▄▄  ▄█▄████
#████▄█▄ ▀▀▄▀▀ █▄  ▄█▀▀█▀ █  ███▀ ████
#████ ▄▄█▄▀▄█ ▄▄▀ █▄ ▄▄█ ▀▄  ▄███▄████
#████▄▄██▄ ▄▀  ▄██ ▄ ▀▀▄▀▄▄ ▀██▀▀ ████
#████▄▄█▄▀▄▄▀ ▄ ▄█▀█ ▀█▀▄▀█▀█ ▄██▄████
#████▄▄▄█▄▄▄█▀▀█▄ ▄█▀ ▄▀█ ▄▄▄  ▀▄▀████
#████ ▄▄▄▄▄ █▀▀▀▀ ▄ ▄ ██▀ █▄█ ███▄████
#████ █   █ ██ ▀██   ▀██   ▄▄  ▀▄▀████
#████ █▄▄▄█ █ ▄█▄█▀█ █▄▀█▀▄█▀ ▀█▄▄████
#████▄▄▄▄▄▄▄█▄██▄▄▄█▄▄███▄███▄▄██▄████
#█████████████████████████████████████

#############BIBLIOTECAS
import random#BIBIOTECA PARA GERAR NUMEROS ALEATORIOS
import os#BIBLIOTECA PARA USAR OPERACOES DO SISTEMA
from Tkinter import *#BIBLIOTECA DO TKINTER

#############FUNTES
FONT1 = ['Ubuntu',12,'bold']#FONTE
FONT2 = ['Ubuntu',10,'bold']#FONTE
FONT3 = ['Verdana',6,'bold']#FONTE

#############JANELA INICIAL
Main = Tk()#CRIA A INSTANCIA DE TK (JANELA)
Main['bg'] = 'white'#DA A COR
Main.geometry("400x773")#TAMANHO
Main.title("Sistemas Operacionais - SJF")#TITULO DA JANELA
				
#############FUNCOES 
#FUNCAO QUE LISTA OS PROCESSOS E OS CPUBUSTER
# class _Scan:
def Scan():
	itemm = 0
	contador = 0#CRIA UM CONTADOR
	numeros = []#CRIA UMA ARRAY
	pro = int(ETY_PRO.get())#PEGA A INFORMACAO DA LABEL

	os.system("rm SJF.txt && rm turn.txt && rm turnn.txt && rm medWait.txt && rm medTurn.txt")					
	os.system("chmod +x waiting.sh && chmod +x turnaround.sh 2>/dev/null")
	
	for ran in range(pro):#for 'ran' EM 'range' ATE 'pro'
	    numero = int(random.randrange(1,101))#'numero' RECEBE UM NUMERO RANDOMICO DE 1 A 100
	    for chave, valor in enumerate(numeros):#FOR PARA ENUMERAR, CRIA 'char' E 'valor'
	        if numero < valor:#SE 'numero' FOR MENOR QUE 'valor' 
	            numeros.insert(chave, numero)#'numeros' EH INSERIDO em 'chave' E 'numero'  
	            break     #PARA
	    else: #SE NAO
	        numeros.append(numero)#'mumero' EH ADICIONADO EM 'numeros'
	
	arquivo = open('turn.txt', 'a')#ABRE O ARQUIVO 'SJF.txt' COM PERMISSAO DE LEITARA E ESCRITA
	arquivo.write('0\n')#ESCREVE TUDO O QUE ESTA EM 'contador' E 'item'
	arquivo.close()#FECHA O ARQUIVO    

	   

	while contador < pro:	#ENQUANTO 'contador' FOR MENOR QUE 'pro'
		for item in numeros:#FOR DE 'item' EM 'numeros'
			contador = contador + 1#CONTADOR, 'contador' RECEBE ELE MESMO +1
			#GERA UM ARQUIVO E SALVA 
			arquivo = open('SJF.txt', 'a')#ABRE O ARQUIVO 'SJF.txt' COM PERMISSAO DE LEITARA E ESCRITA
			arquivo.write("       P%s                   %s           \n" %(contador,item))#ESCREVE TUDO O QUE ESTA EM 'contador' E 'item'
			arquivo.close()#FECHA O ARQUIVO
			arquivo = open('SJF.txt', 'r')#ABRE O ARQUIVO 'STF.txt' COM PERMISSAO DE LEITURA
			leitura = arquivo.read()#LE TUDO QUE ESTA NO ARQUIVO
			LBL_LeituraPro['text'] = leitura#TROCA A CHAVE 'text' DO LABEL 'LBL_Leitura'
			arquivo.close()#FECHA O ARQUIVO

			itemm = itemm+item

			arquivo = open('turn.txt', 'a')#ABRE O ARQUIVO 'SJF.txt' COM PERMISSAO DE LEITARA E ESCRITA
			arquivo.write("%s\n" %itemm)#ESCREVE TUDO O QUE ESTA EM 'contador' E 'item'
			arquivo.close()#FECHA O ARQUIVO

			os.system("rm tturn.txt 2>/dev/null")
			os.system("cat turn.txt | head -n -1 >> tturn.txt")

			arquivo = open('tturn.txt', 'r')#ABRE O ARQUIVO 'STF.txt' COM PERMISSAO DE LEITURA
			leitura = arquivo.read()#LE TUDO QUE ESTA NO ARQUIVO
			LBL_LeituraWait['text'] = leitura#TROCA A CHAVE 'text' DO LABEL 'LBL_Leitura'
			arquivo.close()#FECHA O ARQUIVO
	
			arquivo = open('turnn.txt', 'a')#ABRE O ARQUIVO 'SJF.txt' COM PERMISSAO DE LEITARA E ESCRITA
			arquivo.write("%s\n" %itemm)#ESCREVE TUDO O QUE ESTA EM 'contador' E 'item'
			arquivo.close()#FECHA O ARQUIVO
			arquivo = open('turnn.txt', 'r')#ABRE O ARQUIVO 'STF.txt' COM PERMISSAO DE LEITURA
			leitura = arquivo.read()#LE TUDO QUE ESTA NO ARQUIVO
			LBL_LeituraTurn['text'] = leitura#TROCA A CHAVE 'text' DO LABEL 'LBL_Leitura'
			arquivo.close()#FECHA O ARQUIVO

		os.system("./waiting.sh >> medWait.txt") 
		os.system("./turnaround.sh >> medTurn.txt") 

		arquivo = open('medWait.txt', 'r')#ABRE O ARQUIVO 'STF.txt' COM PERMISSAO DE LEITURA
		leitura = arquivo.read()#LE TUDO QUE ESTA NO ARQUIVO
		LBL_LeituraAveWait['text'] = leitura#TROCA A CHAVE 'text' DO LABEL 'LBL_Leitura'
		arquivo.close()#FECHA O ARQUIVO
		
		arquivo = open('medTurn.txt', 'r')#ABRE O ARQUIVO 'STF.txt' COM PERMISSAO DE LEITURA
		leitura = arquivo.read()#LE TUDO QUE ESTA NO ARQUIVO
		LBL_LeituraAveTurn['text'] = leitura#TROCA A CHAVE 'text' DO LABEL 'LBL_Leitura'
		arquivo.close()#FECHA O ARQUIVO
	
#############LABELS	
#NUMERO DE PROCESSOS
LBL_PRO = Label(Main,text = 'Numero de Processos:')#NOME
LBL_PRO['bg'] = 'white'#COR
LBL_PRO.place(x = 7,y = 10)#LOCAL X,Y
LBL_PRO['font'] = FONT2#FONTE

#ENTRADA DE DADOS
ETY_PRO = Entry(Main,width = 12)#ENTRADA
ETY_PRO.insert(END,'1-34')#TEXTO DETRO
ETY_PRO['font'] = FONT2#FONTE
ETY_PRO.place(x = 180,y = 10)#LOCAL X,Y

#ESCALONAMENTO SJF
LBL_SJF = Label(Main,text = 'Escalonamento SJF',font = FONT1,bg = 'white',fg = 'red').place(x = 10,y = 70)#NOME

#LINHA DE DIVISAO
LBL_Linha = Label(Main,width = 90,bg = 'red').place(x = 0, y = 125,height = 0)#LINHA COM LOCAL X,Y
LBL_Linhaa = Label(Main,width = 600,bg = 'blue').place(x = 0, y = 700,height = 0)#LINHA COM LOCAL X,Y

#KARAN LUCIANO | JACKSON DURAES
LBL_Developers = Label(Main,text = 'Karan Luciano | Jackson Duraes',bg = 'white', fg = 'red',font = ("Verdana",6,"bold"))#NOMES
LBL_Developers.place(x = 240, y = 115)#LOCAL X,Y

#PROCESSOS | CPUBUSTER
LBL_Open = Label(Main,text = ' Process  |  Buster  |  Waiting  |  Turnaround',font = FONT1,bg = 'white')#NOME
LBL_Open.place(x = 10, y = 140)#LOCAL X,Y

#ESPACO EM BRANCO DE LEITURA
LBL_LeituraPro = Label(Main, text='', bg='white')#ESPACO EM BRANCO
LBL_LeituraPro.place(x=5, y=165)#LOCAL X,Y

LBL_LeituraWait = Label(Main, text='', bg='white')#ESPACO EM BRANCO
LBL_LeituraWait.place(x=214, y=165)#LOCAL X,Y

LBL_LeituraTurn = Label(Main, text='', bg='white')#ESPACO EM BRANCO
LBL_LeituraTurn.place(x=317, y=165)#LOCAL X,Y

LBL_LeituraAveWait = Label(Main, text='', bg='white',font = FONT2)#ESPACO EM BRANCO
LBL_LeituraAveWait.place(x=190, y=715)#LOCAL X,Y

LBL_LeituraAveTurn = Label(Main, text='', bg='white',font = FONT2)#ESPACO EM BRANCO
LBL_LeituraAveTurn.place(x=190, y=733)#LOCAL X,Y

#############BOTOES
#BOTAO 'Gerar'
BTO_Scan = Button(Main,text = 'GERAR',width = 7,height = 3)#NOME
BTO_Scan['command'] = Scan#,SJF#ATRABUI O COMANDO BOTAO, CHAMANDO A FUNCAO 'Scan' 
BTO_Scan['font'] = FONT1#TIPO DE FONTE
BTO_Scan.place(x = 298, y = 10)#LOCAL X,Y

Main.mainloop()#CHAMA Tk::

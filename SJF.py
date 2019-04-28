# encoding: utf-8

#####	NAME:				ALGORITMO DE ESCALONAMENTO SHORTEST JOB FIRST (SJF)
#####	VERSION:			1.0
#####	DESCRIPTION:		O ALGORITMO APRESENTA A ORDEM DA EXECUCAO DOS PROCESSOS, CONFORME ESTRATEGIA DE ESCALONAMENTO
#####	DATE OF CREATION:	27/04/2019
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
Main.geometry("400x853")#TAMANHO
Main.title("Sistemas Operacionais - SJF")#TITULO DA JANELA

#############TRATAMENTO
#VERIFICA SE EXISTE O ARQUIVO NO CAMINHO, SE EXISTIR ELE EH APAGADO
for raiz, diretorio, arquivos in os.walk('/home/karan/Documentos/operacionais'):
		for arquivo in arquivos:#FOR ARQUIVO EM ARQUIVOS
			if arquivo.endswith('SJF.txt'):#SE ENCONTRAR O ARQUIVO
				os.remove(os.path.join(raiz,arquivo))#O ARQUIVO EH APAGADO

#############FUNCOES 
#FUNCAO QUE LISTA OS PROCESSOS E OS CPUBUSTER
# class _Scan:
def Scan():
	contador = 0#CRIA UM CONTADOR
	numeros = []#CRIA UMA ARRAY
	pro = int(ETY_PRO.get())#PEGA A INFORMACAO DA LABEL

	#VERIFICA SE EXISTE O ARQUIVO NO CAMINHO, SE EXISTIR ELE EH APAGADO
	for raiz, diretorio, arquivos in os.walk('/home/karan/Documentos/operacionais'):
		for arquivo in arquivos:#FOR ARQUIVO EM ARQUIVOS
			if arquivo.endswith('SJF.txt'):#SE ENCONTRAR O ARQUIVO
				os.remove(os.path.join(raiz,arquivo))#O ARQUIVO EH APAGADO

	for ran in range(pro):#for 'ran' EM 'range' ATE 'pro'
	    numero = int(random.randrange(1,101))#'numero' RECEBE UM NUMERO RANDOMICO DE 1 A 100
	    for chave, valor in enumerate(numeros):#FOR PARA ENUMERAR, CRIA 'char' E 'valor'
	        if numero < valor:#SE 'numero' FOR MENOR QUE 'valor' 
	            numeros.insert(chave, numero)#'numeros' EH INSERIDO em 'chave' E 'numero'  
	            break     #PARA
	    else: #SE NAO
	        numeros.append(numero)#'mumero' EH ADICIONADO EM 'numeros'
	while contador < pro:	#ENQUANTO 'contador' FOR MENOR QUE 'pro'
		for item in numeros:#FOR DE 'item' EM 'numeros'
			contador = contador + 1#CONTADOR, 'contador' RECEBE ELE MESMO +1
			#GERA UM ARQUIVO E SALVA 
			arquivo = open('SJF.txt', 'a')#ABRE O ARQUIVO 'SJF.txt' COM PERMISSAO DE LEITARA E ESCRITA
			arquivo.write("P%s --------------------> %s\n" %(contador,item))#ESCREVE TUDO O QUE ESTA EM 'contador' E 'item'
			arquivo.close()#FECHA O ARQUIVO
			
			arquivo = open('SJF.txt', 'r')#ABRE O ARQUIVO 'STF.txt' COM PERMISSAO DE LEITURA
			leitura = arquivo.read()#LE TUDO QUE ESTA NO ARQUIVO
			LBL_Leitura['text'] = leitura#TROCA A CHAVE 'text' DO LABEL 'LBL_Leitura'
			arquivo.close()#FECHA O ARQUIVO

	#PARTE QUE FAZ O CALCULO MEDIO SJF DOS PROCESSOS
	escolhido = 0
	y = 1
	n = int(ETY_PRO.get())
	tmpExe = []
	tmpEnt = []

	for x in xrange(1,n+1):
		tmpEnt.append(float(y))
		tmpExe.append(numero+1)

	entradas = list(tmpEnt)
	tempos = list(tmpExe)
	for j in range(0,n): #ORDENA AS OS TEMPOS COM BASE NO TEMPO DE PROCESSO (DO MENOR PARA O MAIOR)
		for i in range(0,n-1):
			if tempos[i]>tempos[i+1]: 
				Aux = tempos[i+1] 	#TROCA O TEMPO
				tempos[i+1] = tempos[i]
				tempos[i] = Aux
				Aux = entradas[i+1] #TROCA A ENTRADA
				entradas[i+1] = entradas[i]
				entradas[i] = Aux	
	soma = 0
	relogio = 0
	for x in xrange(0,n):
		for y in xrange(0,n):
			if entradas[y] <= relogio and entradas[y]>=0:
				escolha = y
				break
			pass
		relogio += tempos[escolhido] #INCREMENTA O RELOGIO COM O TEMPO DE EXECUCAO DO PROCESSO
		soma += relogio - entradas[escolhido]
		entradas[escolhido]=-1
		final = soma/n
		arquivo = open('SJFF.txt', 'w')#ABRE O ARQUIVO 'SJF.txt' COM PERMISSAO DE LEITARA E ESCRITA
		arquivo.write("%s\n" %final)#ESCREVE TUDO O QUE ESTA EM 'contador' E 'item'
		arquivo.close()#FECHA O ARQUIVO
		arquivo = open('SJFF.txt', 'r')#ABRE O ARQUIVO 'STF.txt' COM PERMISSAO DE LEITURA
		leitura = arquivo.read()#LE TUDO QUE ESTA NO ARQUIVO
		LBL_Leituraa['text'] = ("%su.t"%leitura)#TROCA A CHAVE 'text' DO LABEL 'LBL_Leitura'
		arquivo.close()#FECHA O ARQUIV		
			
#############LABELS	
#NUMERO DE PROCESSOS
LBL_PRO = Label(Main,text = 'Numero de Processos:')#NOME
LBL_PRO['bg'] = 'white'#COR
LBL_PRO.place(x = 7,y = 10)#LOCAL X,Y
LBL_PRO['font'] = FONT2#FONTE

#ENTRADA DE DADOS
ETY_PRO = Entry(Main,width = 12)#ENTRADA
ETY_PRO.insert(END,'1')#TEXTO DETRO
ETY_PRO['font'] = FONT2#FONTE
ETY_PRO.place(x = 180,y = 10)#LOCAL X,Y

#ESCALONAMENTO SJF
LBL_SJF = Label(Main,text = 'Escalonamento SJF',font = FONT1,bg = 'white',fg = 'red').place(x = 10,y = 70)#NOME

#LINHA DE DIVISAO
LBL_Linha = Label(Main,width = 90,bg = 'red').place(x = 0, y = 125,height = 0)#LINHA COM LOCAL X,Y

#KARAN LUCIANO | JACKSON DURAES
LBL_Developers = Label(Main,text = 'Karan Luciano | Jackson Duraes',bg = 'white', fg = 'red',font = ("Verdana",6,"bold"))#NOMES
LBL_Developers.place(x = 165, y = 115)#LOCAL X,Y

#PROCESSOS | CPUBUSTER
LBL_Open = Label(Main,text = 'Processo | CPUBuster      Tempo Medio',font = FONT1,bg = 'white')#NOME
LBL_Open.place(x = 39, y = 140)#LOCAL X,Y

#ESPACO EM BRANCO DE LEITURA
LBL_Leitura = Label(Main, text='', bg='white')#ESPACO EM BRANCO
LBL_Leitura.place(x=60, y=160)#LOCAL X,Y

LBL_Leituraa = Label(Main, text='', bg='white',font = FONT1)#ESPACO EM BRANCO
LBL_Leituraa.place(x=260, y=175)#LOCAL X,Y

#############BOTOES
#BOTAO 'Gerar'
BTO_Scan = Button(Main,text = 'GERAR',width = 7,height = 3)#NOME
BTO_Scan['command'] = Scan#,SJF#ATRABUI O COMANDO BOTAO, CHAMANDO A FUNCAO 'Scan' 
BTO_Scan['font'] = FONT1#TIPO DE FONTE
BTO_Scan.place(x = 300, y = 10)#LOCAL X,Y

Main.mainloop()#CHAMA Tk

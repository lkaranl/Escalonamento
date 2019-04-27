#####	NAME:				ALGORITMO DE ESCALONAMENTO SHORTEST JOB FIRST (SJF)
#####	VERSION:			1.0
#####	DESCRIPTION:		O ALGORITMO APRESENTA A ORDEM DA EXECUCAO DOS PROCESSOS, CONFORME ESTRATEGIA DE ESCALONAMENTO
#####	DATE OF CREATION:	27/04/2019
#####	WRITTEN BY:			KARAN LUCIANO SILVA | JACKSON DURAES
#####	E-MAIL:				karanluciano1@gmail.com			
#####	DISTRO:				MANJARO LINUX
#####	LICENSE:			GPLv3 			
#####	PROJECT:			https://github.com/lkaranl/Vector_Clock

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
#CUNAO 'Scan'
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
	    numero = int(random.randrange(1,100))#'numero' RECEBE UM NUMERO RANDOMICO DE 1 A 100
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
			arquivo = open('/home/karan/Documentos/operacionais/SJF.txt', 'a')#ABRE O ARQUIVO 'SJF.txt' COM PERMISSAO DE LEITARA E ESCRITA
			arquivo.write("P%s --------------------> %s\n" %(contador,item))#ESCREVE TUDO O QUE ESTA EM 'contador' E 'item'
			arquivo.close()#FECHA O ARQUIVO

#FUNCAO 'Lei'
def Lei():
	arquivo = open('SJF.txt', 'r')#ABRE O ARQUIVO 'STF.txt' COM PERMISSAO DE LEITURA
	leitura = arquivo.read()#LE TUDO QUE ESTA NO ARQUIVO
	LBL_Leitura['text'] = leitura#TROCA A CHAVE 'text' DO LABEL 'LBL_Leitura'
	arquivo.close()#FECHA O ARQUIVO


#############LABELS	
#NUMERO DE PROCESSOS
LBL_PRO = Label(Main,text = 'Numero de Processos:')#NOME
LBL_PRO['bg'] = 'white'#COR
LBL_PRO.place(x = 0,y = 10)#LOCAL X,Y
LBL_PRO['font'] = FONT2#FONTE

#ENTRADA DE DADOS
ETY_PRO = Entry(Main,width = 13)#ENTRADA
ETY_PRO.insert(END,'1-46')#TEXTO DETRO
ETY_PRO['font'] = FONT2#FONTE
ETY_PRO.place(x = 180,y = 10)#LOCAL X,Y

#ESCALONAMENTO SJF
LBL_SJF = Label(Main,text = 'Escalonamento SJF',font = FONT1,bg = 'white',fg = 'red').place(x = 10,y = 80)#NOME

#LINHA DE DIVISAO
LBL_Linha = Label(Main,width = 90,bg = 'red').place(x = 0, y = 125,height = 0)#LINHA COM LOCAL X,Y

#KARAN LUCIANO | JACKSON DURAES
LBL_Developers = Label(Main,text = 'Karan Luciano | Jackson Duraes',bg = 'white', fg = 'red',font = ("Verdana",6,"bold"))#NOMES
LBL_Developers.place(x = 165, y = 115)#LOCAL X,Y

#PROCESSOS | CPUBUSTER
LBL_Open = Label(Main,text = 'Processo | CPUBuster',font = FONT1,bg = 'white')#NOME
LBL_Open.place(x = 100, y = 140)#LOCAL X,Y

#ESPACO EM BRANCO DE LEITURA
LBL_Leitura = Label(Main, text='', bg='white')#ESPACO EM BRANCO
LBL_Leitura.place(x=120, y=160)#LOCAL X,Y


#############BOTOES
#BOTAO 'Gerar'
BTO_Scan = Button(Main,text = 'Gerar',width = 5,height = 2)#NOME
BTO_Scan['command'] = Scan#ATRABUI O COMANDO BOTAO, CHAMANDO A FUNCAO 'Scan' 
BTO_Scan['font'] = FONT1#TIPO DE FONTE
BTO_Scan.place(x = 315, y = 10)#LOCAL X,Y

#BOTAO 'Exibir'
BTO_Exib = Button(Main,text = 'Exibir',width = 5,height = 2)#NOME
BTO_Exib['command'] = Lei#ATRABUI O COMANDO BOTAO, CHAMANDO A FUNCAO 'Lei'
BTO_Exib['font'] = FONT1#TIPO DE FONTE
BTO_Exib.place(x = 315, y = 70)#LOCAL X,Y

Main.mainloop()#CHAMA Tk
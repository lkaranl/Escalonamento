#!/usr/bin/env bash
  
DADOS=turnaround.txt
N=$(wc -l $DADOS | cut -d " " -f 1)
SOMA=$(paste -sd+ $DADOS | bc)
MEDIA=$(echo "scale=1; $SOMA/$N" | bc)
echo "Average Turnaround: $MEDIA" 

#wc -l CONTA O NUMERO DE LINHAS NO ARQUIVO, cut faz o tratamento para sobrar apenas o digito
#FAZ A SOMA DE TODOS OS VALORES NO ARQUIVO
#FAZ O CALCULO DA MEDIA COM ESCALA DE CASA DECIMAIS
#MOSTRA A MEDIA 

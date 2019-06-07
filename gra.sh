#!/usr/bin/env bash

gnuplot -persist <<-EOFMarker
	set key left
	set xlabel 'PROCESSO'
	set ylabel 'TURNAROUND / WAITING / BUSTER'
	set terminal wxt  enhanced title "Turnaround" persist raise
    plot "turnaround.txt" title 'Tournaround (roxo)' with lines smooth csplines, 'waiting.txt' title 'Waiting (verde)' with lines smooth csplines, 'buster.txt' title 'Buster (azul)' with lines smooth csplines
EOFMarker

#CENTRALIZA OS TITLES
#LABEL DO EIXO X
#LABEL DO EIXO Y
#TITULO DA JANELA
#FAZ AS LINHAS DE ACORDO COM OS VALORES INFORMADOS NOS ARQUIVOS

#!/bin/bash
  
DADOS=/home/karan/Documentos/operacionais/turnn.txt
N=$(wc -l $DADOS | cut -d " " -f 1)
SOMA=$(paste -sd+ $DADOS | bc)
MEDIA=$(echo "scale=2; $SOMA/$N" | bc)
echo "Average Turnaround: $MEDIA" 
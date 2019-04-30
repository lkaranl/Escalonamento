#!/bin/bash
  
DADOS=/home/karan/Documentos/operacionais/tturn.txt
N=$(wc -l $DADOS | cut -d " " -f 1)
SOMA=$(paste -sd+ $DADOS | bc)
MEDIA=$(echo "scale=2; $SOMA/$N" | bc)
echo "Average Waiting: $MEDIA" 
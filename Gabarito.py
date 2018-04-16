# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""


import numpy as np
import pandas as pd
import math 
import matplotlib.pyplot as plt


#Importando os dados dos pokemons
dataset = pd.read_csv('pokemon.csv.csv', encoding = 'ISO-8859-1') 
investida=40; #Poder de ataque da investida
lvlmod = ((2*100)/5)+2 #Modificador do level para a fórmula

#Criação de uma nova base de dados, na qual contaremos o número de vitórias de cada pokémon
legenda1=['pokedexNum','nome','numerodevitorias']
datasetvitorias=pd.DataFrame(index= dataset.index, columns=legenda1)
datasetvitorias.iloc[:,0]=dataset.iloc[:,0]
datasetvitorias.iloc[:,1]=dataset.iloc[:,1]



for i in range(len(dataset)):
    #Stats do primeiro Pokémon;
    ataquepokemon1=dataset.iloc[i][5]
    hppokemon1=dataset.iloc[i][4]
    defesapokemon1=dataset.iloc[i][6]
    velpokemon1=dataset.iloc[i][9]
    tipo1pokemon1=dataset.iloc[i][2]
    tipo2pokemon1=dataset.iloc[i][3]
    vitorias=0; #Contador de vitórias
    #Bônus por ser normal para o pokémon 1:
    if tipo1pokemon1 == 'Normal':
        stab1=1.5
    else:
        stab1=1
    #Consideração do tipo do primeiro pokémon
    if tipo1pokemon1=='Rock' or tipo2pokemon1 =='Rock' or tipo1pokemon1=='Steel' or tipo1pokemon1=='Steel':
        rockmod1=0.5
    else:
        rockmod1=1;
         
    for j in range (len(dataset)):
        if i!=j: #O pokémon não pode batalhar contra ele mesmo
            
            #Stats do segundo Pokémon;
            ataquepokemon2=dataset.iloc[j][5]
            hppokemon2=dataset.iloc[j][4]
            defesapokemon2=dataset.iloc[j][6]
            velpokemon2=dataset.iloc[j][9]
            tipo1pokemon2=dataset.iloc[j][2]
            tipo2pokemon2=dataset.iloc[j][3]
            
            #Modificador de Tipo:
            if tipo1pokemon2=='Rock' or tipo2pokemon2 =='Rock' or tipo1pokemon2=='Steel' or tipo1pokemon2=='Steel':
                rockmod2=0.5
            else:
                rockmod2=1;
            #Bônus por ser normal para o pokémon 2:
            if tipo1pokemon2 == 'Normal':
                stab2=1.5
            else:
                stab2=1
            # Simulação da batalha:
            
            #Cáculo dos modificadores de dano:
            mod1 = stab1*rockmod2
            mod2 = stab2*rockmod1
            
            #Cálculo da quantidade de dano por ataque:
            danopokemon1 = ((lvlmod*investida*(ataquepokemon1/defesapokemon2))/50+2)*mod1
            danopokemon2 = ((lvlmod*investida*(ataquepokemon2/defesapokemon1))/50+2)*mod2
            
            #Cálculo do número de ataques necessários para matar um pokémon:
            #Necessário arrendondar para cima
            numataque1=math.ceil(hppokemon2/danopokemon1)
            numataque2=math.ceil(hppokemon1/danopokemon2)
            
            #Critério de desempate - O pokémon com mais speed ataca primeiro,
            #Matando o outro mais rapidamente
            if numataque1==numataque2:
                if velpokemon1>velpokemon2:
                    vitorias+=1
            else: 
                if numataque1<numataque2:
                    vitorias+=1;
        #Adicionando no dataset o número de vitórias:
        datasetvitorias.iloc[i,2]=vitorias
            
 # Gráfico - Análise Geral
eixoX=datasetvitorias[:,0]
eixoy=datasetvitorias[:,1]
plt.scatter(eixoX,eixoy, color = 'red')
#plt.plot(eixoX, eixoy, color = 'blue')
plt.title('O melhor pokémon')
plt.xlabel('Número do pokémon')
plt.ylabel('Número de vitórias')
plt.show()
            
            
            
    
    
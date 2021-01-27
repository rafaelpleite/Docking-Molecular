# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 15:58:42 2020

@author: Anderson Lima
"""
'''Estrutura 2 para o Docking, algumas correções para usso mais util'''
'fazer o script se torna executavel'
'''correções:
    -corrigir a saida dos aminoacidos
    -verificar o uso da coluna de ligante e aminoacidos
    '''
import pandas as pd
def main():
    name = input('insira o diretório do arquivo: ')
    saida_1 = input('insira o diretório para saida do arquivo sem as repetições:\n ')
    saida_2 = input('insira o diretório para saida do arquivo com os aminoacidos:\n ')
    saida_3 = input('insira o diretório para saida do arquivo da lista de aminoacidos:\n ')
    
    resultado = limpa_dados(name)
    repete = aminoacidos_aparições(resultado)
    amino = amino_total(resultado)
    aparições, ami = amino[0], amino[1]  #o aminoacidos são uma lista de aminoacidos que aparecerão
    aminoacido = aminoacidos(ami)
    repete.to_csv(saida_1)
    aparições.to_csv(saida_2)
    aminoacido.to_csv(saida_3)

def limpa_dados (dados):
    df = pd.read_csv(dados)
    Proteinas = {'ALA','ARG','ASN','ASP','GLU','CYS','GLY','GLN','HIS','LLE',
                 'LEU','LYS','MET','PHE','PRO','SER','TYR','THR','TRP','VAL'}
    
    filtro_from = df['From'].str.split(':',expand = True)[1].str[:3].isin(Proteinas)
    filtro_To = df['To'].str.split(':',expand = True)[1].str[:3].isin(Proteinas)
    ligante_from = df[filtro_To]['From'].copy()
    ligante_To = df[filtro_To]['To'].copy()
    df.loc[filtro_To,'From'] = ligante_To
    df.loc[filtro_To,'To'] = ligante_from
    
    df_final = df[filtro_from != filtro_To]
    return df_final

def aminoacidos_aparições(df):
    dados = df
    aminoacidos,ligantes,tipo_ligação = list(dados['From'].str.split(':')),list(dados['To'].str.split(':')),list(dados['Types'])
    proteina, ligante, tipo, n, ligações = [],[],[],[],[]
    for i in range(len(ligantes)):
        ligação = (aminoacidos[i][1],ligantes[i][1],tipo_ligação[i])
        if ligação not in ligações:
            ligações.append(ligação)
            proteina.append(aminoacidos[i][1])
            ligante.append(ligantes[i][1])
            tipo.append(tipo_ligação[i])
            n.append(1)
        else:
            for l in range(len(proteina)):
                if (proteina[l],ligante[l],tipo[l]) == ligação:
                    n[l] = n[l] + 1
    data = {'Aminoacido':proteina, 'Ligante':ligante,'tipo de ligação':tipo, 'N° Ligações': n}
    df_retorna = pd.DataFrame(data, columns=['Aminoacido', 'Ligante', 'tipo de ligação','N° Ligações'])
    return df_retorna

def amino_total(df):
    dados = df
    aminoacidos,ligantes,tipo_ligação = list(dados['From'].str.split(':')),list(dados['To'].str.split(':')),list(dados['Types'])
    proteina, ligante, tipo, n, ligações = [],[],[],[],[]
    for i in range(len(ligantes)):
        ligação = (aminoacidos[i][1],tipo_ligação[i])
        if ligação not in ligações:
            ligações.append(ligação)
            proteina.append(aminoacidos[i][1])
            tipo.append(tipo_ligação[i])
            n.append(1)
        else:
            for l in range(len(proteina)):
                if (proteina[l],tipo[l]) == ligação:
                    n[l] = n[l] + 1
    amino = proteina
    data = {'Aminoacido':proteina,'Tipo de ligação':tipo, 'N° Ligações': n}
    df_retorna = pd.DataFrame(data, columns=['Aminoacido', 'Tipo de ligação','N° Ligações'])
    return (df_retorna,amino)

def aminoacidos(lista):
    aminoacido = []
    for i in range(len(lista)):
        if lista[i] not in aminoacido:
            aminoacido.append(lista[i])
    data = {"Aminoacidos": aminoacido}
    df_retorna = pd.DataFrame(data, columns = ['Aminoacidos'])
    return df_retorna

if __name__ == '__main__':
    main()
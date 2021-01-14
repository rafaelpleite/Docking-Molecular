# -*- coding: cp1252 -*-

"""
Programa para fazer simulacoes com o AutoDock Vina
O arquivo SimularAutodock.py deve ficar na mesma pasta que o ligante, receptor, config.txt e o arquivo "vina.exe".
"""
import time
from subprocess import *
import subprocess
import platform
import os
import shlex

x0, y0, z0 = 10, 0, -30
x1, y1, z1 = 70, 120, 40
pulo = 10  #O programa começa na posicao [x0, y0, z0] depois [x0, y0, z0 + pulo], e assim por diante...
tempo = 10

def main():
    dirNome = 'Resultados'
    if not os.path.exists(dirNome): #Cria uma pasta Resultados para depositar os resultados do Docking
        os.mkdir(dirNome)
        print("Diretório" , dirNome ,  " criado.")
    else:
        print("Diretório" , dirNome ,  "Já exite.")
    print('=-'*30)
    print('Simulações de diversas posições com AutodockVina.')
    print('Edite o programa no seu editor de Python antes de usa-lo.')
    print('Certifique-se de executar apenas o arquivo "SimularAutodock.py" quando for rodar o programa')
    print('=-'*30)
    if platform.system() == 'Windows': calc_pos_WINDOWS() #Verifica o sistema, se Windows, entÃ£o chama a funÃ§Ã£o calc_pos_WINDOWS(), senÃ£o, chama calc_pos_LINUX(). NÃ£o sei se calc_pos_LINUX() funciona em MACOS.
    else: calc_pos_LINUX()
    insert = input('Tecle ENTER para finalizar')

def calc_pos_WINDOWS():
    '''IMPORTANTE como se trata de muitas execuÃ§Ãµes do
    Vina entre com um intervalo entre as simulaÃ§Ãµes. Isso pode ser feito calculando o tempo de uma simulaÃ§Ã£o completa.
    Assim evita-se o risco do computador travar devido a processos simultÃ¢neos no processador.'''
    global x0, y0, z0, x1, y1, z1, pulo, tempo
    for i in range(x0, x1+1, pulo):
        for j in range(y0, y1+1, pulo):
            for k in range(z0, z1+1, pulo):
                Popen('cmd /k "vina.exe" --config config.txt --center_x '+ str(i)+' --center_y '+ str(j)+' --center_z '+ str(k)+
                  ' --out Resultados\proteina-ligante,'+str(i)+','+str(j)+','+str(k)+',.pdbqt --log Resultados\log,'+str(i)+','+str(j)+','+str(k)+',.txt && exit')
                """
                Adiciona as posicoes do teste na lista M para um uso posterior.
                Executa o cmd e digita o seguinte comando no terminal
                "vina.exe" --config config.txt --center_x [pos_x] --center_y [pos_y] -- center_z [pos_z]
                --out proteina-ligante[pos_x][pos_y][pos_z].pdbqt --log log[pos_x][pos_y][pos_z].txt
                """
                time.sleep(tempo)
    time.sleep(5)
    print('Terminou! \nTempo de excuÃ§Ã£o: {} s'.format(time.perf_counter() - t0))

def calc_pos_LINUX():
    global x0, y0, z0, x1, y1, z1, pulo
    for i in range(x0, x1+1, pulo):
        for j in range(y0, y1+1, pulo):
            for k in range(z0, z1+1, pulo):
                subprocess.call(shlex.split('vina --config config.txt --center_x '+ str(i)+' --center_y '+ str(j)+' --center_z '+ str(k)+ ' --out Resultados/proteina-ligante,'+str(i)+','+str(j)+','+str(k)+',.pdbqt --log Resultados/log,'+str(i)+','+str(j)+','+str(k)+',.txt'))
                #print(f'{i} {j} {k} feito.')
                """
                Adiciona as posicoes do teste na lista M para um uso posterior.
                Executa o cmd e digita o seguinte comando no terminal
                "vina.exe" --config config.txt --center_x [pos_x] --center_y [pos_y] -- center_z [pos_z]
                --out proteina-ligante[pos_x][pos_y][pos_z].pdbqt --log log[pos_x][pos_y][pos_z].txt
                """

if __name__ == '__main__':
    main()

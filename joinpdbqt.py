"""
@author: Rafael

Recebe um diretório com arquivos .pdbqt e retorna um único arquivo .pdbqt de todos os resultados.
"""

import os

path = 'C:\SARSCOV2\OAII\LuteolinPLProPOOL\LuteolinPLpro\Teste\Resultados'
limit = float(-7.5)

def main():
    arc, data_load = str(), []
    for root, directories, files in os.walk(path, topdown=False):
        if root == path:
            for names in files:
                if names.find('pdbqt') != -1:
                    for i in load(str(path + r'/b'[0] + names)): data_load.append(i)
    for i, d in enumerate(data_load):
        arc = arc + str('MODEL ') + str(i+1) + d[1:]

    with open('ligand_out.pdbqt', 'w+') as f:
        f.write(str(arc))


def load(i):
    global limit
    with open(i) as fp: data = fp.read()
    data = data.split('MODEL ')
    data.pop(0)
    arq = []
    for j, jval in enumerate(data):
        if float(jval[26:34]) <= limit:
            arq.append(jval)
    if len(arq) != 0:
        return arq
    else: return ''
    


main()
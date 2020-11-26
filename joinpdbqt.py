"""
@author: Rafael

Recebe um diretório com arquivos .pdbqt e retorna um único arquivo .pdbqt de todos os resultados.
"""

import os


path = 'C:\SARSCOV2\Favipiravir\FavipiravirPLpro\Teste\Resultado'

def main():
    arc, data_load = str(), []
    for root, directories, files in os.walk(path, topdown=False):
        if root == path:
            for names in files:
                if names.find('pdbqt') != -1:
                    for i in load(str(path + r'/b'[0] + names)): data_load.append(i)
    for i, d in enumerate(data_load):
        arc = arc + str('MODEL ') + str(i+1) + d[1:] + '\n'

    with open('ligand_out.pdbqt', 'w+') as f:
        f.write(str(arc))


def load(i):
    data = ''
    with open(i) as fp:
        data = fp.read()
    data = data.split('MODEL ')
    data.pop(0)
    return data
main()
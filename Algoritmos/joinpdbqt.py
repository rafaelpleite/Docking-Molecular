import pandas as pd
import os

df = pd.read_csv(r'C:\Users\Rafael\Desktop\sitio_catalitico.csv')
df = df[(df['Ligand'] == 'CN340')]

path = r'C:\Users\Rafael\Nanobio\Nsp15_dockings\OPT\pdbqt_opt_renew'
protein = r'C:\Users\Rafael\Nanobio\Nsp15_dockings\OPT\6w01_prot.pdbqt'
pdbqt = 'MODEL PROTEIN\n'

with open(protein) as p:
    pdbqt += p.read()
    p.close()

for u in df[df.duplicated(subset=['Ligand']) == False]['Ligand']:
    pdbqt += f'MODEL {u}\n'
    df_u = df[df['Ligand'] == u]
    for v in df_u[df_u.duplicated(subset=['Name']) == False]['Name']:
        df_v = df_u[df_u['Name'] == v]
        count = list(df_v['Count'])
        path_uv = os.path.join(path, u, v + str('.pdbqt'))
        with open(path_uv) as w:
            data = w.read().split('MODEL ')
            for x in count:
                pdbqt += data[int(x)][2:]
            w.close()    
open(r'C:\Users\Rafael\Desktop\out.pdbqt', 'w+').write(pdbqt)
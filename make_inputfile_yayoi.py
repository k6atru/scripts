#%%
# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
# import sys
# homedir = os.environ['HOME']
# #os.path.joinの2つめの引数には/をつけない
# pipdir = os.path.join(homedir, ".local/lib/python3.8/site-packages")
# sys.path.append(pipdir)
import Bio.PDB as pdb

currentdir = os.getcwd()

#%%
if os.path.isfile(currentdir + "/.DS_Store") == True:
    os.remove(currentdir + "/.DS_Store")

iddir_list = []
iddir_list = os.listdir(currentdir)

# for文を回してリスト要素の削除を行うとリストのインデックス番号がずれてしまうため、バグる
# for i, j in enumerate(iddir_list):
#     iddir_list[i] = os.path.join(currentdir, j)

# for i, j in enumerate(iddir_list):
#     if os.path.isfile(j) == True:
#         iddir_list.pop(i)

data_list = []
iddir_list = []
data_list = os.listdir(currentdir)

for i, j in enumerate(data_list):
    data_list[i] = os.path.join(currentdir, j)

for i, j in enumerate(data_list):
    if os.path.isdir(j) == True:
        iddir_list += [j]

#%%
# iddir_list.remove(currentdir + "/Bio")
#__pycache__を削除
if currentdir + "/__pycache__" in iddir_list:
    iddir_list.remove(currentdir + "/__pycache__")

# iddir_listからピリオドで始まる要素を削除
for i, j in enumerate(iddir_list):
    if os.path.basename(j).startswith(".") == True:
        iddir_list.pop(i)

#%%

for d in iddir_list:
    pdbid = os.path.basename(d)
    pdbfile = os.path.join(d, "amber", "pr", "init.pdb")
    print(pdbfile)

    pdb_parser = pdb.PDBParser()
    try:
        struct = pdb_parser.get_structure("all", pdbfile)
    except FileNotFoundError:
        print("FileNotFoundError")
        continue
    chain = struct[0].get_list()[0]
    res = chain.get_list()
    for r in res:
        if r.get_resname() == "FPP":
            fppid = str(r.get_id()[1])

    dihed_script = open(d + "/amber/pr/dihed.in", "w")
    dihed_script.write("trajin ./001/mdcrd 1 last 50\ntrajin ./002/mdcrd 1 last 50\ndihedral dih1 :" + fppid + "@O1 :" + fppid + "@C1 :" + fppid + "@C2 :" + fppid + "@C3 out dihed.txt range360\nstrip :SOD,CLA,WAT,TIP3,Na+,Cl-\n")
    dihed_script.close()

    four_dist_script = open(d + "/amber/pr/4dist.in", "w")
    four_dist_script.write("trajin ./001/mdcrd 1 last 50\ntrajin ./002/mdcrd 1 last 50\n# C1toC6\ndistance dist1 :" + fppid + "@C1 :" + fppid + "@C7 out 4dist.txt\n# C1toC7\ndistance dist2 :" + fppid + "@C1 :" + fppid + "@C8 out 4dist.txt\n# C1toC10\ndistance dist3 :" + fppid + "@C1 :" + fppid + "@C12 out 4dist.txt\n# C1toC11\ndistance dist4 :" + fppid + "@C1 :" + fppid + "@C13 out 4dist.txt\n")
    four_dist_script.close()
    print(pdbid + " is done")
#%%

    # pm = pymol2.PyMOL()
    # pm.start()
    # pm.cmd.load(pdbfile, f"{pdbid}")
    # pm.cmd.select("fpp", "resn FPP")

    # pm.cmd
    # pm.stop()

    #pymolでFPPを選択して、そのインデックス番号を取得

    #インデックスを元に、pdbファイルを読み込み、FPPの座標を取得

# %%
# # %%
# os.path.isdir('/Users/toneyusuke/Desktop/test/4dist.in')
# # %%

# pdbid = os.path(d)

# %%
import Bio.PDB
# %%

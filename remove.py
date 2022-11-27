# #%%
# from multiprocessing.connection import answer_challenge
# from operator import mod
# import pdb
# from select import select
# from tracemalloc import start
# from turtle import pd
# import pymol
# from pymol import cmd as cmd
# import os
# from Bio.PDB import *
# from Bio.Seq import Seq
# import pymol2

# #%%
# # for i in range(len(dir_list)):
# #   if "pre_leap" == os.path.splitext(dir_list[i])[0]: ## os.path.splitext()[1]で拡張子を取得
# #     pdb_file = os.path.join(dir_list[i])

# #%%
# pdb_parser = PDBParser()
# structure = pdb_parser.get_structure('X', 'test.pdb')
# model = structure[0].get_list()
# chain = model[0].get_list()
# residue = chain[0].get_list()


# #%%
# for r in chain:
#     print(r.get_resname())
# #%%
# res = structure.get_residues()
# print(res)

# #%%
# print(len(chain))
# #%%
# residues = structure.chains[0].get_list()
# for r in residues:
#     print(r.get_id())

# #%%
# pymol.finish_launching()

# cmd.load("test.pdb", "master")

# #%%
# cmd.select("fpp", "resn FPP")
# #%%
# last = str(len(chain))
# last30 = str(len(chain) - 30)
# answer = "resi " + last30 + ":" + last

# cmd.select("start", answer)
# #%%
# print(answer)
# cmd.select("start")
# # %%
# cmd.select("outs","byres resn * within 5.0 of resn fpp")
# cmd.select("not (resn outs) and start")
# #%%
# cmd.delete("start and outs")
# # %%
# p1 = pymol2.PyMOL()
# p1.start()
# p1.cmd.fragment('ala')
# p1.cmd.zoom()
# p1.cmd.png('ala.png', 1000, 800, dpi=150, ray=1)
# p1.stop()


# # %%
# p2 = pymol2.PyMOL()
# p2.start()
# p2.cmd.load("test.pdb", "aaa")
# p2.cmd.zoom()
# p2.cmd.png("aaa.png", 1000, 800, dpi=300, ray=1)
# p2.stop
# %%
import os
from threading import currentThread
import pymol2
import Bio.PDB

currentdir = os.path.abspath("./")
if os.path.isfile(f"{currentdir}/.DS_Store") == True:
    os.remove(currentdir + "/.DS_Store")
dirlist = os.listdir(currentdir)
pdbfiles = []

def get_end(pdbfile_path):
    pdb_parser = Bio.PDB.PDBParser()
    struct = pdb_parser.get_structure("seq", pdbfile_path)
    res = struct[0]["A"].get_list()
    length = -4
    for r in res:
        length += 1
    return length

for d in dirlist:
    iddir_list = []

    iddir = os.path.join(currentdir, d)
    try:
        iddir_list += os.listdir(iddir)
    except:
        pass
    for f in iddir_list:
        if "pre_leap.pdb" == f:
            pdbfiles.append(os.path.join(iddir, f))

for (i, pdbfile) in enumerate(pdbfiles):
    iddir = os.path.dirname(pdbfile)

    pymol_i = f"pymol_{i}"
    exec("pymol_i = pymol2.PyMOL()")

    pymol_i.start()
    pymol_i.cmd.load(pdbfile, "protain")

    pymol_i.cmd.select("fpp", "resn FPP")
    len = get_end(pdbfile)

    pymol_i.cmd.select("start30", "resi 1:20")
    pymol_i.cmd.select("end30", f"resi {len-20}:len")
    pymol_i.cmd.select("7A_aroundfpp", "byres resn * within 7.0 of fpp")

    pymol_i.cmd.select("remove1", "start30 and (not 7A_aroundfpp)")
    pymol_i.cmd.select("remove2", "end30 and (not 7A_aroundfpp)")

    pymol_i.cmd.select("newprotain", "protain and (not remove1) and (not remove2)")

    pymol_i.cmd.save(f"{iddir}/pre_leap.pdb", "newprotain")
    pymol_i.stop()

# # %%
# import os
# import pymol2
# import Bio.PDB

# def get_end(pdbfile_path):
#     pdb_parser = Bio.PDB.PDBParser()
#     struct = pdb_parser.get_structure("seq", pdbfile_path)
#     res = struct[0]["A"].get_list()
#     length = -4
#     for r in res:
#         length += 1
#     return length

# pymol_i = pymol2.PyMOL()
# pymol_i.start()
# pymol_i.cmd.load("./test.pdb", "protain")

# pymol_i.cmd.select("fpp", "resn FPP")
# len = get_end("test.pdb")

# pymol_i.cmd.select("start30", "resi 1:30")
# pymol_i.cmd.select("end30", f"resi {len-30}:len")
# pymol_i.cmd.select("10A_aroundfpp", "byres resn * within 7.0 of fpp")

# pymol_i.cmd.select("remove1", "start30 and (not 7A_aroundfpp)")
# pymol_i.cmd.select("remove2", "end30 and (not 7A_aroundfpp)")

# pymol_i.cmd.select("newprotain", "protain and (not remove1) and (not remove2)")

# pymol_i.cmd.save("pre_leap.pdb", "newprotain")
# pymol_i.stop()


# #%%

# # %%
# print(currentdir)
# # %%

# %%
print(pdbfiles)
# %%
print(os.path.dirname(pdbfiles[0]))
# %%

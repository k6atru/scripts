#%%
import os
import shutil

data_dir = "/data/tone"
arranged_dir = "/data/tone/arranged"

ID_list = [line.rstrip() for line in open(os.path.join(arranged_dir, "list.txt"))]
print(ID_list)



# %%
pdb_data_dir = "/data/tone/pdb_data"
os.makedirs(pdb_data_dir, exist_ok=True)
# %%
for ID in ID_list:
    ID_dir = os.path.join(arranged_dir, ID)  #IDのMD結果が入っているディレクトリ

    dir_list = os.listdir(ID_dir)  #更新日時ごとのIDのMD結果が入っているディレクトリのリスト
    dir_list = [os.path.join(ID_dir, d) for d in dir_list]  #フルパスに変換

    ID_ddir = os.path.join(pdb_data_dir, ID)  #これからこのIDのMDの結果がコピーされるディレクトリ

    for d in dir_list:
        init_pdb_path = os.path.join(d, "amber/pr/init.pdb")
        init_trr_path = os.path.join(d, "amber/pr/traj.trr")
        yymmdd = os.path.basename(d)
        # 更新日時を名前とするディレクトリを作る
        os.makedirs(os.path.join(ID_ddir, yymmdd), exist_ok=True)
        # init.pdbをコピー
        try:
            shutil.copy2(init_pdb_path, os.path.join(ID_ddir, yymmdd))
        except FileNotFoundError:
            print(f"{ID} {yymmdd} init.pdb not found")
        # traj.trrをコピー
        try:
            shutil.copy2(init_trr_path, os.path.join(ID_ddir, yymmdd))
        except FileNotFoundError:
            print(f"{ID} {yymmdd} traj.trr not found")



# %%

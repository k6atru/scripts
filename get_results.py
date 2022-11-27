# %%
#再帰的にディレクトリ取得
from codecs import getdecoder
import os
import re

def get_dir_list(path):
    dir_list = []
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            dir_list.append(os.path.join(root, dir))
    return dir_list

currentdir = os.path.abspath(os.path.curdir)

#currentdirにresultという名前のフォルダがあるか確認
if not "result" in os.listdir(currentdir):
    #なければresultというディレクトリを作成
    os.mkdir(os.path.join(currentdir, "result"))
result_dir = os.path.join(currentdir, "result")

#list.txtをreadlinesする
with open('list.txt') as f:
    lines = f.readlines()

#list.txtの中身をforで回す
for id in lines:
    # idの中に改行が入っているので削除
    id = id.rstrip()
    #現在のディレクトリにあるディレクトリを再帰的に取得
    dirs = get_dir_list(currentdir)
    #idを含むディレクトリを取得
    id_dirs = [d for d in dirs if id in d]
    #id_dirsからidよりあとの任意の文字列を削除
    id_dirs = [re.sub(f"{id}/.*", f"{id}", d) for d in id_dirs]
    #id_dirsから重複を削除して作成日時の古い順にソート
    id_dirs = sorted(list(set(id_dirs)), key=os.path.getctime)
    #id_dirsにcurrentdirのresultが含まれる要素を削除
    id_dirs = [d for d in id_dirs if not result_dir in d]
    #resultディレクトリにidという名前のディレクトリを作成
    #あるか確認
    if not id in os.listdir(result_dir):
        os.mkdir(os.path.join(result_dir, id))
    id_result_dir = os.path.join(result_dir, id)

    #id_dirsのディレクトリをforで回す
    for i, id_dir in enumerate(id_dirs):
        #idのディレクトリの中にamber/pr/dihed.txtがあるか確認
        if os.path.exists(os.path.join(id_dir, "amber/pr/dihed.txt")):
            #あればresultディレクトリにコピー
            os.system(f"cp {os.path.join(id_dir, 'amber/pr/dihed.txt')} {id_result_dir}")
            #id_dirsに複数のディレクトリがある場合は番号をつける
            if len(id_dirs) > 1:
                os.rename(os.path.join(id_result_dir, "dihed.txt"),
                          os.path.join(id_result_dir, f"dihed_{i}.txt"))
#%%
print(len(id_dirs))
# %%
# dirs
# # %%
# dirs = get_dir_list(currentdir)
# # %%
# # %%
# # list.txtを読み込んでIDリストを取得
# IDs = [line.rstrip() for line in open('list.txt')]
# # IDsをforで回して、現在のディレクトリの下にあるIDのフォルダを取得
# for ID in IDs:
#     # 現在のディレクトリの下にある全てのフォルダからIDという名前のディレクトリのフルパスをリストに格納
#     dirs = [os.path.join(os.getcwd(), d)
#             for d in os.listdir(os.getcwd()) if ID in d]
#     for i, dir in enumerate(dirs):
#         dir = os.path.join(dir, "amber/pr/dihed.txt")
#         dirs[i] = dir
#     print(dirs)


# # %%
# scp / data/tone/A0A097ZQD8/amber/pr/dihed.txt toneyusuke@192.168.0.231: / Users/toneyusuke/Desktop/

# %%

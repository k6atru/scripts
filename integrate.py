# %%
import os

# ディレクトリ直下のフォルダのリストを取得
dir_list = os.listdir()
# ファイルを除外
dir_list = [d for d in dir_list if os.path.isdir(d)]

# "."から始まるフォルダとファイルを除外
dir_list = [d for d in dir_list if not d.startswith(".")]
# %%
print(dir_list)

# %%
dist_path = "/data/tone/raw_data"

# dist_pathの中のフォルダのうち、dir_listに含まれるもののパスを取得
for d in dir_list:
    if d in os.listdir(dist_path):
        dist_dir = os.path.join(dist_path, d)
    # dのフォルダの中身をすべてdist_dirに移動
    for f in os.listdir(d):
        os.rename(os.path.join(d, f), os.path.join(dist_dir, f))

# %%

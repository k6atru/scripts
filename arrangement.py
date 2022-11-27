#%%
from datetime import datetime
import os
import shutil
#%%
#listを読み込む
IDs = []
IDs = [line.rstrip() for line in open('list.txt')]
print(IDs)
for ID in IDs:
    print(f"{ID} is in working....")
    ID_dirs = []
    #./arrangedにIDのディレクトリを作成
    os.makedirs('./arranged/' + ID, exist_ok=True)
    #現在のディレクトリに含まれるディレクトリからIDを含むものを再帰的に検索
    for root, dirs, files in os.walk(".", topdown=False):
        for name in dirs:
            if ID in name:
                ID_dirs.append(os.path.join(root, name))
    try:
        ID_dirs.remove(f"./result/{ID}")
    except ValueError:
        print("result directories not found")
    try:
        ID_dirs.remove(f"./arranged/{ID}")
    except ValueError:
        print("arranged directories not found")

    print(f"moving{ID_dirs}")
    #ID_dirsの要素をパスとして、arranged/ID/にコピー
    for ID_dir in ID_dirs:
        #作成日時を取得
        ctime = os.path.getctime(ID_dir)
        #作成日時を6桁の文字列に変換
        ctime_str = datetime.fromtimestamp(ctime).strftime('%y%m%d')
        #作成日時のフォルダを作成
        os.makedirs(f"./arranged/{ID}/{ctime_str}", exist_ok=True)
        #ディレクトリとファイルをコピー
        shutil.copytree(ID_dir, f"./arranged/{ID}/{ctime_str}", dirs_exist_ok=True )
        #ディレクトリを削除
        shutil.rmtree(ID_dir)
    print(f"{ID} is done")


# %%

module load amber22
#list.txtを読み込む
for i in `cat list.txt`
do
#listにある名前のディレクトリに移動
cd $i/amber/pr
#cpptrajを実行
cpptraj -i ./trajfix.in -p ../../top/leap.parm7
#for終了
cd ../../..
done

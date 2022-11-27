#!/usr/bin/bash
# This script will create a trajectory file for a given set of coordinates

#ディレクトリ内のディレクトリのリストをフルで取得、forでループ
for dir in `ls -d $PWD/*/`; do
    #ANSIエスケープシーケンスを$dirから除去して、dir名を取得
    # dir_name=`echo $dir | sed -e 's/\x1b\[[0-9;]*m//g'`
    #dirに移動
    cd $dir
    python ~/GitHub/preparemd/run_preparemd.py --file=$dir/pre_leap.pdb --distdir=./ --fftype="ff19SB" --num_mddir=2 --ns_per_mddir=50 --boxsize="80 80 80" --ion_conc=150 --machineenv="yayoi" --mol2="FPP = loadMol2 /Users/toneyusuke/Workbench/templete/top/fpp.mol2"
    cd ../
done

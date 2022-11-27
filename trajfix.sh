#!/usr/bin/bash
# This script will create a trajectory file for a given set of coordinates

#ディレクトリ内のディレクトリのリストをフルで取得、forでループ、cdでdirへ移動
for dir in `ls -d $PWD/*/`; do
    #ANSIエスケープシーケンスを$dirから除去して、dir名を取得
    dir_name=`echo $dir | sed -e 's/\x1b\[[0-9;]*m//g'`

    cd $dir_name
    #dirの中のamber/prに移動
    cd amber/pr

    cpptraj -p ../../top/leap.parm7 -i trajfix.in
done

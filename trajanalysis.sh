#!/usr/bin/bash
# This script will create a trajectory file for a given set of coordinates

#ディレクトリ内のディレクトリのリストをフルで取得、forでループ、cdでdirへ移動
for dir in `ls -d $PWD/*`; do
    #dirの中のamber/prに移動
    cd $dir_name
    cd amber/pr
    #ANSIエスケープシーケンスを$dirから除去して、dir名を取得
    dir_name=`echo $dir | sed -e 's/\x1b\[[0-9;]*m//g'`
    id=dirname $dir_name
    cpptraj -p ../../top/leap.parm7 -i dihed.in
    cpptraj -p ../../top/leap.parm7 -i 4dist.in
    scp -p 4dist.txt /Users/toneyusuke/Desktop/dat/$id
    scp -p dihed.txt /Users/toneyusuke/Desktop/dat/$id
done
cd /data/tone/1023

#!/bin/bash
#用于提交脚本运行
mkdir  RawRules

for ii in {0..12}
do
        nohup python AlarmTrain.py $ii &
done

python AlarmTrain.py 13

python AlarmAdd.py

python AlarmReudec.py
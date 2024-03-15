#!/bin/bash
pace1=5
pace2=10
pace3=15
pace4=20
pace5=25
pace6=30
pace7=35
pace8=40
pace9=45
pace10=50

pace=$pace1
select_count=150

cur_count=0
filename="predict_$select_count$pace.txt"

while [ $cur_count -le $select_count ]
do
  #cur_count=`expr $cur_count + $pace` OK
  cur_count=$((cur_count+$pace))
  #echo $cur_count
  python3 run.py -c $cur_count >> $filename

done

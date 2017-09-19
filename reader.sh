#!/bin/bash
#echo 0
dir=/home/pi/nfcpy/experiments3
file_name=$(date '+%Y%m%d%H%M').csv
#echo 1
#jobs -l | awk '{print "sudo kill " $2;}'|sh
#ps -afx | grep felicareader | grep -v grep | sed 2d | awk '{print "asudo kill" $1;}'|sh
#echo 2
sudo rsync -aruz -e 'ssh -p 443 -i /home/pi/.ssh/id_rsa' $dir morimoto@153.126.194.52:/home/morimoto/exp
#echo 3
sudo python /home/pi/nfcpy/felicareader8.py $dir/$file_name &
#echo 4

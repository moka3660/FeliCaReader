#!/bin/bash
#echo 0
sakura=XXXXX
dir=/home/pi/nfcpy/FeliCaReader/septem1/ras0
file_name=$(date '+%Y%m%d%H%M').csv
#echo 1
sudo rsync -aruz -e 'ssh -p 443 -i /home/pi/.ssh/id_rsa0' $dir sakura:/home/morimoto/septem1/
#echo 2
sudo python /home/pi/nfcpy/FeliCaReader/idm_reader.py $dir/$file_name &
#echo 3

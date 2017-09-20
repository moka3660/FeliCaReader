#!/bin/bash
#echo 0
dir=/home/pi/nfcpy/FeliCaReader/septem1
file_name=$(date '+%Y%m%d%H%M').csv
#echo 1
sudo rsync -aruz -e 'ssh -p 443 -i /home/pi/.ssh/id_rsa' $dir morimoto@153.126.194.52:/home/morimoto/
#echo 2
sudo python /home/pi/nfcpy/FeliCaReader/idm_reader.py $dir/$file_name &
#echo 3

#!/bin/sh

#  wakeAllOnHost.sh
#  
#
#  Created by Hans-Filip Elo on 2014-07-07.
#

if [ -z "$1" ]
then
    echo ""
    echo "Wakes all machines on remote ESXi-host. Created by hansfilipelo & tobyndax"
    echo ""
	echo "Usage: "
	echo "      ./wakeAllOnHost.sh"
    echo ""
    exit 1
fi

ESXHOST=$1

# Start VMs again
echo ""
ssh root@$ESXHOST << 'ENDSSH'
# Define variables
VMLIST=/tmp/vmlist.txt
touch $VMLIST

# Gets id of all running VMs
vim-cmd vmsvc/getallvms | tail -n +2 > $VMLIST

while read line
do
    echo "Starting $(echo $line | awk '{print $2}') "
    vim-cmd vmsvc/power.on $(echo $line | awk '{print $1}')
    echo "Started VM $(date "+%Y-%m-%d %H:%M")"
    echo " - "
done < $VMLIST

rm $VMLIST
ENDSSH

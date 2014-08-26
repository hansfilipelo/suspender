#!/usr/bin/python

#  suspender.py
#
#  Multi-threaded suspender for VMware ESXi virtual machines. Suspends all machines on a given host.
#
#  Created by hansfilipelo & tobyndax, 2014-08-25.
#

import sys, os
from time import gmtime, strftime

# ----------------
# Helper functions

def threader(pool,vmList):
    file = open(vmList)

    for line in file.readlines():
        data = line.split()

        id = data[0]
        vmName = data[1]
        pool.apply_async(suspender, args=(id,vmName))

def suspender(id,vmName):
    print("Suspending machine " + vmName + " " + strftime("%Y-%m-%d %H:%M", gmtime()))
    os.system("ssh root@" + hostname + " vim-cmd vmsvc/power.suspend " + id + " | grep -v 'Suspending VM:'")
    print("Finished suspending machine " + vmName + " " + strftime("%Y-%m-%d %H:%M", gmtime()))

# ----------------

if len(sys.argv) != 3:
    print ""
    print "Multi-threaded suspender for VMware ESXi virtual machines. Suspends all machines on a given host. "
    print ""
    print "Created by: hansfilipelo & tobyndax"
    print ""
    print "Usage: "
    print "    python suspender.py esxiHostname nrOfSimoultaniousSuspends"
    print ""
    sys.exit

else:
    hostname = sys.argv[1]
    nrOfSimoultaniousSuspends = int(sys.argv[2])
    vmList = "/tmp/vmlist.dat"
    
    os.system("touch %s" %vmList)
    os.system("ssh root@" + hostname + " vim-cmd vmsvc/getallvms | tail -n +2 > " + vmList)
    
    if __name__ == "__main__":
        import multiprocessing as mp
        pool = mp.Pool(nrOfSimoultaniousSuspends)
        threader(pool,vmList)
        pool.close()
        pool.join()

        os.system("rm " + vmList)
